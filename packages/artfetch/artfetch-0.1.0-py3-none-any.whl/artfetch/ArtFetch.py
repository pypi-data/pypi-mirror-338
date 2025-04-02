import argparse
import asyncio
import webbrowser
from pathlib import Path
from typing import List

import mutagen
from PIL import Image
from mutagen import MutagenError
from mutagen.id3 import APIC

from .configuration import config, write_config
from .sources import SourceCandidate
from .sources.bandcamp import Bandcamp
from .sources.discogs import Discogs, authorize_discogs
from .sources.musicbrainz import MusicBrainz
from .view import View

app_name = "artfetch"
version_number = "0.1"

source_map = {
    'bandcamp': Bandcamp,
    'discogs': Discogs,
    'musicbrainz': MusicBrainz
}


def main():
    parser = argparse.ArgumentParser(
        description=f""" {app_name}  /path/to/directory""",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        prog=f'{app_name}'
    )
    parser.add_argument('path', type=str, help="Path to the folder you want to parse")
    parser.add_argument('-f', '--force', default=False, action='store_true',
                        help="Process all files, not just the ones without album art.")
    parser.add_argument('-r', '--recursive', default=False, action='store_true',
                        help="Process Files in Directory and all Subdirectories")
    parser.add_argument('-a', '--auto', default=False, action='store_true',
                        help="Omit user selection and always select the best match as album art source.")
    parser.add_argument('-u', '--ui', default=False, action='store_true',
                        help="Use the default view if your terminal does not support modern features like colors. Or if you prefer a scrolling interface.")
    parser.add_argument('-m', '--manual', default=False, action='store_true',
                        help="Do not use auto selection, even if enabled in config file.")
    config.read(user=True)
    # writes the default config to the config path if no config files exists
    write_config(config, False)
    args = parser.parse_args()
    ui = View((args.auto or config['auto']['enable'].get(bool))and not args.manual)
    authorize_discogs(ui)
    try:
        if config['rich-interface'].get(bool) or args.ui:
            with ui.start_display():
                process_directory(args, ui)

        else:
            process_directory(args, ui)

    finally:
        ui.stop_display()


def process_directory(args, ui):
    path = Path(args.path)
    if not path.exists():
        ui.print_err('Path ' + args.path + ' is not valid ')
        return
    if not path.is_dir():
        ui.print_err(f"[not a valid path")
    sources = []
    for key, source_class in source_map.items():
        if config['sources'][key].get(bool):
            sources.append(source_class)
    iterate_over_directory(path, args, ui, sources)


async def get_image_sources(sources, tag):
    return await asyncio.gather(*(asyncio.to_thread(cls, tag) for cls in sources))


async def process_candidate(candidate: SourceCandidate):
    await candidate.pull_artwork()
    return candidate


async def pull_all_artwork(all_candidates):
    tasks = [asyncio.create_task(process_candidate(candidate))
             for candidate in all_candidates]
    results = await asyncio.gather(*tasks)
    return results


def iterate_over_directory(path: Path, args, ui, sources):
    # print empty message to init footer
    for file in path.iterdir():
        ui.set_filename(file.name)
        # holds all the Candidates for the Various online Tag Sources
        all_candidates = []
        # go through subfolders if recursive flag is set
        if file.is_dir() and (config['sub-folder'].get(bool) or args.recursive):
            iterate_over_directory(file, args, ui, sources)
        ui.update_header(file.name)
        audiofile = open_audio_file(file, ui)
        ui.print('')
        if audiofile is None:
            continue
        tag = check_tag_compatibility(audiofile, args, ui)
        if tag is None:
            continue
        ui.show_spinner()
        image_sources = asyncio.run(get_image_sources(sources, tag))
        for source in image_sources:
            all_candidates.extend(source.get_candidates())
        all_candidates.sort(key=lambda candidate: candidate.get_confidence(), reverse=True)
        all_candidates = [candidate for candidate in all_candidates if
                          candidate.get_confidence() >= config['lower-confidence'].get(float)]
        if not all_candidates:
            ui.print_err(f"Did not find any suitable matches")
            continue
        # autotagging selects the result with the highest confidence score
        selected_candidate = None
        if (args.auto or config['auto']['enable'].get(bool))and not args.manual:
            candidate: SourceCandidate
            for candidate in all_candidates:
                if candidate.get_artwork_url() is not None:
                    selected_candidate = candidate
                    break
            if selected_candidate is None:
                ui.print_err("Could not find candidate with artwork")
                continue
            if selected_candidate.get_confidence() >= config['auto']['threshold'].get(float):
                asyncio.run(selected_candidate.pull_artwork())
            else:
                ui.print_err("Confidence in best match was too low")
                continue

        # skip selection if selection-confidence is reached by first result
        else:
            for candidate in all_candidates:
                if candidate.get_artwork_url() is not None and candidate.get_confidence() > config[
                    'selection-confidence'].get(float):
                    selected_candidate = candidate
                    asyncio.run(selected_candidate.pull_artwork())
                    break
            if selected_candidate is None:
                all_candidates = asyncio.run(pull_all_artwork(all_candidates))
                selected_candidate = selection_loop(all_candidates, tag, ui)
        # if either skip was selected or confidence was too low
        if selected_candidate is None:
            continue
        save_info_to_tag(selected_candidate, audiofile, ui)


# check validity of audio file and if it needs to be opened
def open_audio_file(file: Path, ui) -> mutagen.FileType or None:
    if not file.is_file():
        return None
    if file.suffix.lower() != '.mp3':
        return
    try:
        audiofile = mutagen.File(file)
    except MutagenError as e:
        ui.print_err(f"Unable to open {file.name}")
        return None
    if audiofile is None:
        ui.print_err(f"Unable to open {file.name}")
        return None
    if audiofile.tags is None:
        ui.print_err(f"File does not contain ID3 Tags{file.name}")
        return None
    return audiofile


def save_info_to_tag(candidate: SourceCandidate, audiofile, ui):
    if candidate.get_artwork_image() is not None:
        audiofile.tags.add(
            APIC(
                encoding=0,  # 3 = UTF-8
                mime=Image.MIME.get(candidate.get_artwork_image().format),
                # MIME type of the image (e.g., image/jpeg or image/png)
                type=3,  # 3 = Cover (front)
                desc="Cover",
                data=candidate.get_raw_artwork(),  # Read the image data
            )
        )
        try:
            audiofile.save()
        except Exception as e:
            ui.print_err(f"Error writing ID3-Tag: {e}")
        ui.print_success(f"Album Art written..")
    else:
        ui.print_err('Selected Candidate does not have an image ')


def check_tag_compatibility(audiofile, args, ui):
    tag = {}
    for frame in audiofile.tags.values():
        if isinstance(frame, APIC) and not (args.force or config['force'].get(bool)):
            ui.print(f"[bold white]Skipping as album art exists")
            return None
    if 'TALB' not in audiofile.tags and 'TIT2' not in audiofile.tags:
        return None
    if 'TIT2' in audiofile.tags:
        tag['title'] = audiofile.tags['TIT2'].text[0]
    if 'TALB' in audiofile.tags:
        tag['album'] = audiofile.tags['TALB'].text[0]
    if 'TPE1' in audiofile.tags:
        tag['artist'] = audiofile.tags['TPE1'].text[0]
    return tag


def selection_loop(all_candidates: List[SourceCandidate], tag, ui) -> SourceCandidate | None:
    while True:
        ui.print_table(tag, all_candidates)
        indices = list(range(len(all_candidates)))
        indices = [i + 1 for i in indices]
        indices_str = list(map(str, indices))
        selected_option = ui.input(
            f"select candidate [dark_olive_green3 bold]1-{len(all_candidates)}[/dark_olive_green3  bold], [dark_olive_green3 bold]s[/dark_olive_green3 bold]kip, show [dark_olive_green3 bold]i[/dark_olive_green3 bold]mage, open [dark_olive_green3 bold]b[/dark_olive_green3 bold]rowser, [dark_olive_green3 bold]Q[/dark_olive_green3 bold]uit",
            indices_str + (["i", "b", 's', 'q']))
        if selected_option == "i":
            selected_option = int(
                ui.input(f'[bold white]show image of candidate #1-{len(all_candidates)}', indices_str)) - 1
            image = all_candidates[selected_option].get_artwork_image()
            if image is not None:
                # twice the height as image is rendered in half characters
                ui.show_image(image)
            else:
                ui.print_err("[white] no image associated with this")
        elif selected_option == "b":
            selected_option = int(
                ui.input(f'[bold white]open source url of candidate #1-{len(all_candidates)}', indices_str)) - 1
            webbrowser.open(all_candidates[selected_option].get_tag_info()['url'])
        elif selected_option == "s":
            ui.print(f"[bold white]skipping file")
            return None
        elif selected_option == "q":
            exit(0)
        else:
            return all_candidates[int(selected_option) - 1]


async def create_instance_async(source, tag):
    # Assume source() is an async callable or wrap a blocking call appropriately
    return await source(tag)


if __name__ == "__main__":
    main()
