import musicbrainzngs
import requests
from beetsplug.bandcamp.search import get_similarity

from . import user_agent, Source, SourceCandidate, _calc_similarities

musicbrainzngs.set_useragent(user_agent, "0.1", "http://example.com/music")

class MusicBrainz(Source):
    def __init__(self, tag):
        super().__init__(tag)

        for candidate in \
        musicbrainzngs.search_recordings(artist=self._artist, query=self._title, release=self._album, limit=5)[
            "recording-list"]:
            self._candidates.append(MusicBrainzCandidate(candidate, tag))


class MusicBrainzCandidate(SourceCandidate):
    def __init__(self, candidate, tag):
        super().__init__()
        self._source_type = 'Musicbrainz'
        similarities = []
        try:
            if "album" in tag:
                similarities.append(get_similarity(str(tag.get('album')), candidate['release-list'][0]['title']))
            self._info['album'] = candidate['release-list'][0]['title']
            if "artist" in tag:
                similarities.append(get_similarity(str(tag.get('artist')), candidate["artist-credit-phrase"]))
            self._info['artist'] = candidate["artist-credit-phrase"]
            if "title" in tag:
                similarities.append(get_similarity(str(tag.get('title')), candidate["title"]))
            self._info['track'] = candidate["title"]
        except (KeyError, IndexError):
            return
        # Musicbrainz returns artists or track title which do not match at all, so we sort those out
        self._confidence = _calc_similarities(similarities)
        # build the artwork ref link which returns the url to the artwork
        release_id = candidate['release-list'][0]['id']
        artwork = requests.get(f'https://coverartarchive.org/release/{release_id}/front',
                               allow_redirects=False)
        if artwork.status_code == 307:
            self._artwork_url = artwork.headers['Location']
        else:
            self._artwork_url = None
        candidate_id = candidate['id']
        self._info['url'] = f"https://musicbrainz.org/recording/{candidate_id}"

    def get_confidence(self):
        return self._confidence

    def get_artwork_url(self):
        return self._artwork_url
