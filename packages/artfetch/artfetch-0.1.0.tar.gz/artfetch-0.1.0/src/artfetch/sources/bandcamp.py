from beetsplug.bandcamp import metaguru, http_get_text
from beetsplug.bandcamp import search

from . import Source, SourceCandidate, _calc_similarities, _get_similarity

_config = {
    "comments_separator": "\n---\n",
    "include_digital_only_tracks": True,
    "genre": {
        "capitalize": False,
        "maximum": 0,
        "mode": "progressive",
        "always_include": [],
    },
    "truncate_comments": False,
}


class Bandcamp(Source):
    def __init__(self, tag):
        super().__init__(tag)
        for candidate in search.search_bandcamp(query=f"{self._artist} {self._title} {self._album}", search_type="t"):
            self._candidates.append(BandcampCandidate(candidate, tag))


class BandcampCandidate(SourceCandidate):
    def __init__(self, candidate, tag):
        super().__init__()
        self._source_type = 'Bandcamp'
        similarities = []
        self._info = {
            "artist": candidate['artist'],
            'track': candidate['name'],
            'url': candidate['url'],
            'album' : ''
        }
        if candidate['type'] == 'track' and isinstance(candidate.get('album'), str):
            self._info['album'] = candidate.get('album')
        elif isinstance(candidate.get('title'), str):
            self._info['album'] = candidate.get('title')
        if "album" in tag and isinstance(self._info['album'], str):
            similarities.append(_get_similarity(str(tag.get('album')), self._info['album']))
        if "artist" in tag and isinstance(self._info['artist'], str):
            similarities.append(_get_similarity(str(tag.get('artist')), self._info['artist']))
        if "title" in tag and isinstance(self._info['track'], str):
            similarities.append(_get_similarity(str(tag.get('title')), self._info['track']))
        guru = metaguru.Metaguru.from_html(http_get_text(candidate["url"]), _config)
        if guru.image:
            self._artwork_url = guru.image
        if len(similarities) > 0:
            self._confidence = _calc_similarities(similarities)
        else: self._confidence = 0
