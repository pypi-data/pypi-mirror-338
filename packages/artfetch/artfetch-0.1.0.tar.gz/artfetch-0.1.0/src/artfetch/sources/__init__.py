import io
from abc import ABC
from difflib import SequenceMatcher

import aiohttp
from PIL import Image
from requests import Response

user_agent = "ArtFetch"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}


def to_ascii(string: str) -> str:
    """Lowercase and translate non-ascii chars to '?'."""
    return string.lower().encode("ascii", "replace").decode()


def _get_similarity(query: str, result: str) -> float:
    """Return the similarity between two strings normalized to [0, 1].

    We take into account how well the result matches the query, e.g.
        query: "foobar"
        result: "foo bar"
    Similarity is then:
        (2 * (len("foo") / len("foobar")) + len("foo") / len("foo bar")) / 3

    2/3 of the weight is how much of the query is found in the result,
    and 1/3 is a penalty for the non-matching part.
    """
    a, b = to_ascii(query), to_ascii(result)
    if not a or not b:
        return 0
    m = SequenceMatcher(a=a, b=b).find_longest_match(0, len(a), 0, len(b))
    return ((m.size / len(a)) * 2 + m.size / len(b)) / 3


def _calc_similarities(similarities):
    return round(sum(similarities) / len(similarities), 3)


class Source(ABC):
    def __init__(self, tag):
        self._candidates = []
        self._artist = str(tag.get('artist') or '')
        self._title = str(tag.get('title') or '')
        self._album = str(tag.get('album') or '')

    def get_candidates(self):
        return self._candidates


class SourceCandidate(ABC):
    def __init__(self):
        self._info = {
            "artist": '',
            'track': '',
            'album': '',
            'url': ''
        }
        self._source_type = ''
        self._artwork_url = None
        self._artwork: Response = None
        self._artwork_image: Image = None
        self._confidence = 0

    def get_confidence(self) -> float:
        return self._confidence

    def get_tag_info(self):
        return self._info

    def get_source_type(self) -> str:
        return self._source_type

    def get_artwork_url(self):
        return self._artwork_url

    # externalize this function so the image can be loaded by the main loop only on certain conditions, e.g. confidence
    async def pull_artwork(self):
        if self._artwork_url is not None:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                        self._artwork_url, headers=headers
                ) as response:
                    response.raise_for_status()
                    content = await response.read()
            self._artwork = content  # Store raw content or process as needed
            self._artwork_image = Image.open(io.BytesIO(content))

    def get_artwork_image(self) -> Image:
        return self._artwork_image

    def get_raw_artwork(self) -> bytes:
        return io.BytesIO(self._artwork).getvalue()
