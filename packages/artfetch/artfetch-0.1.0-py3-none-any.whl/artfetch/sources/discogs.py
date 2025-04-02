import webbrowser
from json import JSONDecodeError

import discogs_client
from beetsplug.bandcamp.search import get_similarity
from discogs_client import User
from discogs_client.exceptions import DiscogsAPIError

from . import Source, SourceCandidate, user_agent, _calc_similarities
from ..configuration import write_config
from ..view import View

API_KEY = "AFowAVXGvTYVUYuLZgWr"
API_SECRET = "VFncIhOKUMSwIjoEdSxcCNXrLoHBZIHU"

_discogs : discogs_client.Client = None

def authorize_discogs(ui: View):
    from ..configuration import config
    #if discogs is enabled in the settings
    global _discogs
    if not config['sources']['discogs'].get(bool):
        return False
    if config['discogs-api-key'].get() is not None:
        return _login(config)
    if ui.input("No discogs API-Key found. Do you want to use discogs? Y/N",['y','n']) == 'n':
        config['sources']['discogs'] = False
        ui.print('Discogs disabled. You can re-enable it in the config under sources.')
        write_config(config, True)
        return False
    ui.prompt("Discogs API-Key is not set, please authorize via O-Auth. Press Enter to continue", )
    _discogs = discogs_client.Client(
        'ArtAutoTag',
        consumer_key=API_KEY,
        consumer_secret=API_SECRET)
    auth_info = _discogs.get_authorize_url()
    ui.print(f"Please open {auth_info[2]}. Then click on Authorize.")
    webbrowser.open(auth_info[2])
    access_code = ui.prompt("Please Enter the 10 digit access code")
    token, secret = _discogs.get_access_token(access_code)
    config['discogs-api-key'] = token
    config['discogs-api-secret'] = secret
    write_config(config, True)
    return _login(config)


def _login(config):
    global _discogs
    _discogs = discogs_client.Client(
        user_agent,
        token=config['discogs-api-key'].get(str),
        secret=config['discogs-api-secret'].get(str),
        consumer_key=API_KEY,
        consumer_secret=API_SECRET
    )
    if not isinstance(_discogs.identity(), User):
        return False
    return True


class Discogs(Source):
    global _discogs
    def __init__(self, tag):
        super().__init__(tag)
        #if discogs has no api key
        if _discogs is None:
            return
        try:
            for candidate in _discogs.search(artist=self._artist, title=self._album, track=self._title,
                                             type='release').page(1):
                self._candidates.append(DiscogsCandidate(candidate, tag))

        except DiscogsAPIError as e:
            return


class DiscogsCandidate(SourceCandidate):
    def __init__(self, candidate: discogs_client.Release, tag):
        super().__init__()
        self._source_type = 'Discogs'
        similarities = []
        # catch key errors, e.g. if there is no album tag
        try:
            if "album" in tag:
                similarities.append(get_similarity(str(tag.get('album')), candidate.title))
            self._info['album'] = candidate.title

            # look if one of the artists in the release is the best match
            if "artist" in tag:
                artist_similarity = 0
                for artist in candidate.artists:
                    temp_similarity = get_similarity(str(tag.get('artist')), artist.name)
                    if temp_similarity >= artist_similarity:
                        artist_similarity = temp_similarity
                        self._info['artist'] = artist.name
                similarities.append(artist_similarity)

            # look if one of the titles in the release matches the tag and use that for tagging as well as the confidence
            if "title" in tag:
                track_similarity = 0
                for track in candidate.tracklist:
                    temp_similarity = get_similarity(str(tag.get('title')), track.title)
                    if temp_similarity >= track_similarity:
                        track_similarity = temp_similarity
                        self._info['track'] = track.title
                similarities.append(track_similarity)
        except JSONDecodeError:
            # as confidence is initially 0, failed results are automatically sorted out
            return
        self._confidence = _calc_similarities(similarities)
        # some release do not have an image attached
        if len(candidate.images) > 0:
            self._artwork_url = candidate.images[0].get("uri")
        self._info['url'] = candidate.url
