from datetime import datetime

from rich import box
from rich.align import Align
from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.prompt import Prompt
from rich.spinner import Spinner
from rich.table import Table
from rich_pixels import Pixels
import readchar



class View:
    def __init__(self, auto_enabled):
        self._autolog = ''
        self._auto_enabled = auto_enabled
        self._error_buffer = ''
        self.is_live = False
        self._console = Console()
        self._file_name = ''
        self._layout = Layout(name="root")
        self._live = None


    # used for logging purposes

    @staticmethod
    def prompt(message):
        return Prompt.ask(message)

    def set_filename(self, file_name):
        self._file_name = file_name

    def input(self, message, options):
        if self.is_live:
            self._layout["footer"].update(
                Panel(f'[blink]{message}', title="Input", title_align='left', style='slate_blue3', box=box.ROUNDED), )
            while True:
                key = readchar.readkey()
                if key in options:
                    return key

        else:
            return Prompt.ask(
                message,
                default=1, choices=options, show_choices=False)

    def start_display(self):
        self._layout.split(
            Layout(name="header", size=3),
            Layout(name="body", ratio=1),
            Layout(name="footer", size=3)
        )
        self._live = Live(self._layout, auto_refresh=True, transient=False, screen=True,
                          # Takes over the whole screen
                          redirect_stdout=False, vertical_overflow="visible")
        self._layout['body'].update('')
        self._layout['footer'].update('')
        self.is_live = True
        self._live.start()
        return self._live

    def stop_display(self):
        self._live.stop()
        self._live = None
        self._console.print(self._autolog)
        self._console.show_cursor()

    def show_spinner(self):
        if not self._auto_enabled:
            if self.is_live:

                self._layout["body"].update(
                    Align(Spinner("clock", style="bold green"), align='center', vertical='middle'))
            else:
                self._console.print('Loading results')

    def update_header(self, title):
        if self.is_live:
            self._layout["header"].update(Panel(f'[{title}]', title="ArtFetch", box=box.ROUNDED))
        else:
            self._console.rule(f'[{title}]')

    def print_table(self, tag, all_candidates):
        table = Table(title="Search Results", padding=(1, 0, 0, 1), expand=True, box=box.MINIMAL_HEAVY_HEAD)
        table.add_column(" #")
        table.add_column("Image", width=int(self._console.width / 20))
        table.add_column(f"[italic]artist[/italic] \n {str(tag.get('artist') or '')}", justify="left", style="green")
        table.add_column(f"[italic]title[/italic] \n {str(tag.get('title') or '')}", style="blue")
        table.add_column(f"[italic]album[/italic] \n {str(tag.get('album') or '')}", style="yellow")
        table.add_column("Confidence Level", justify="center")
        table.add_column("Source")
        table.add_column("URL")
        for index, candidate in enumerate(all_candidates):
            info = candidate.get_tag_info()
            artwork_image = candidate.get_artwork_image()
            if artwork_image is not None:
                image = Pixels.from_image(artwork_image,
                                          (int(self._console.width / 20), int(self._console.width / 20)), )
            else:
                image = ''
            table.add_row(f"{index + 1}", image, info["artist"], info['track'], info['album'],
                          f"{round(candidate.get_confidence() * 100, 1)}%",
                          f"{candidate.get_source_type()}", f"{info['url']}")
        if self.is_live:
            self._layout["body"].update(table)
        else:
            self._console.print(table)

    def print(self, message):
        if not self._auto_enabled:
            if self.is_live:
                self._layout["footer"].update(Panel(f'{message}', title="AutoTag", title_align='left', box=box.ROUNDED))
            else:
                self._console.print(f"{message}")

    def print_err(self, error_message):
        self._autolog += f"[red]{datetime.now().isoformat()} {self._file_name} --- {error_message}\n"
        if self._auto_enabled:
            if self.is_live:
                self._layout["body"].update(self._autolog)
            else:
                self._console.print(f"[red]{datetime.now().isoformat()} {self._file_name} --- {error_message}\n")
        else:
            if self.is_live:
                self._layout["footer"].update(
                    Panel(f'[red][{error_message}]', style='red', title="Error", box=box.ROUNDED))
            else:
                self._console.print(f"[bold red]{error_message}")

    def print_success(self, message):
        self._autolog += f"[green]{datetime.now().isoformat()} {self._file_name} --- {message} \n"
        if self._auto_enabled:
            if self.is_live:
                self._layout["body"].update(self._autolog)
            else:
                self._console.print(f"[green]{datetime.now().isoformat()} {self._file_name} --- {message} \n")
        else:
            if self.is_live:
                self._layout["footer"].update(
                    Panel(f'[green][{message}]', style='green', title_align='left', title="Success", box=box.ROUNDED))
            else:
                self._console.print(f"[green]{message}")

    def show_image(self, image):
        if self.is_live:
            self._layout["body"].update(
                Panel(Pixels.from_image(image, (self._console.height * 2 - 12, self._console.height * 2 - 12)),
                      padding=(0, 0, 0, 0), box=box.SIMPLE))
            self.print('Press any key to continue ..')
            while True:
                if readchar.readkey():
                    return
