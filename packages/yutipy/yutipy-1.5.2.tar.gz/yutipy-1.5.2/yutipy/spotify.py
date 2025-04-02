__all__ = ["Spotify", "SpotifyException"]

import base64
import os
import time
from pprint import pprint
from typing import Optional, Union

import requests
from dotenv import load_dotenv

from yutipy.exceptions import (
    AuthenticationException,
    InvalidResponseException,
    InvalidValueException,
    NetworkException,
    SpotifyException,
)
from yutipy.models import MusicInfo
from yutipy.utils.helpers import (
    are_strings_similar,
    guess_album_type,
    is_valid_string,
    separate_artists,
)
from yutipy.utils.logger import logger

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")


class Spotify:
    """
    A class to interact with the Spotify API. It uses "Client Credentials" grant type (or flow).

    This class reads the ``SPOTIFY_CLIENT_ID`` and ``SPOTIFY_CLIENT_SECRET`` from environment variables or the ``.env`` file by default.
    Alternatively, you can manually provide these values when creating an object.
    """

    def __init__(
        self,
        client_id: str = SPOTIFY_CLIENT_ID,
        client_secret: str = SPOTIFY_CLIENT_SECRET,
    ) -> None:
        """
        Initializes the Spotify class (using Client Credentials grant type/flow) and sets up the session.

        Parameters
        ----------
        client_id : str, optional
            The Client ID for the Spotify API. Defaults to ``SPOTIFY_CLIENT_ID`` from environment variable or the ``.env`` file.
        client_secret : str, optional
            The Client secret for the Spotify API. Defaults to ``SPOTIFY_CLIENT_SECRET`` from environment variable or the ``.env`` file.
        """
        if not client_id or not client_secret:
            raise SpotifyException(
                "Failed to read `SPOTIFY_CLIENT_ID` and/or `SPOTIFY_CLIENT_SECRET` from environment variables. Client ID and Client Secret must be provided."
            )

        self.client_id = client_id
        self.client_secret = client_secret
        self._session = requests.Session()
        self.api_url = "https://api.spotify.com/v1"
        self.__header, self.__expires_in = self.__authenticate()
        self.__start_time = time.time()
        self._is_session_closed = False
        self.normalize_non_english = True
        self._translation_session = requests.Session()

    def __enter__(self):
        """Enters the runtime context related to this object."""
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """Exits the runtime context related to this object."""
        self.close_session()

    def close_session(self) -> None:
        """Closes the current session(s)."""
        if not self.is_session_closed:
            self._session.close()
            self._translation_session.close()
            self._is_session_closed = True

    @property
    def is_session_closed(self) -> bool:
        """Checks if the session is closed."""
        return self._is_session_closed

    def __authenticate(self) -> tuple:
        """
        Authenticates with the Spotify API and returns the authorization header.

        Returns
        -------
        dict
            The authorization header.
        """
        try:
            token, expires_in = self.__get_spotify_token()
            return {"Authorization": f"Bearer {token}"}, expires_in
        except Exception as e:
            raise AuthenticationException(
                "Failed to authenticate with Spotify API"
            ) from e

    def __get_spotify_token(self) -> tuple:
        """
        Gets the Spotify API token.

        Returns
        -------
        str
            The Spotify API token.
        """
        auth_string = f"{self.client_id}:{self.client_secret}"
        auth_base64 = base64.b64encode(auth_string.encode("utf-8")).decode("utf-8")

        url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": f"Basic {auth_base64}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {"grant_type": "client_credentials"}

        try:
            logger.info("Authenticating with Spotify API")
            response = self._session.post(
                url=url, headers=headers, data=data, timeout=30
            )
            logger.debug(f"Authentication response status code: {response.status_code}")
            response.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"Network error during Spotify authentication: {e}")
            raise NetworkException(f"Network error occurred: {e}")

        try:
            response_json = response.json()
            return response_json.get("access_token"), response_json.get("expires_in")
        except (KeyError, ValueError) as e:
            raise InvalidResponseException(f"Invalid response received: {e}")

    def __refresh_token_if_expired(self):
        """Refreshes the token if it has expired."""
        if time.time() - self.__start_time >= self.__expires_in:
            self.__header, self.__expires_in = self.__authenticate()
            self.__start_time = time.time()

    def search(
        self,
        artist: str,
        song: str,
        limit: int = 10,
        normalize_non_english: bool = True,
    ) -> Optional[MusicInfo]:
        """
        Searches for a song by artist and title.

        Parameters
        ----------
        artist : str
            The name of the artist.
        song : str
            The title of the song.
        limit: int, optional
            The number of items to retrieve from API. ``limit >=1 and <= 50``. Default is ``10``.
        normalize_non_english : bool, optional
            Whether to normalize non-English characters for comparison. Default is ``True``.

        Returns
        -------
        Optional[MusicInfo_]
            The music information if found, otherwise None.
        """
        if not is_valid_string(artist) or not is_valid_string(song):
            raise InvalidValueException(
                "Artist and song names must be valid strings and can't be empty."
            )

        self.normalize_non_english = normalize_non_english

        music_info = None
        artist_ids = None
        queries = [
            f"?q=artist:{artist} track:{song}&type=track&limit={limit}",
            f"?q=artist:{artist} album:{song}&type=album&limit={limit}",
        ]

        for query in queries:
            if music_info:
                return music_info

            self.__refresh_token_if_expired()

            query_url = f"{self.api_url}/search{query}"

            logger.info(
                f"Searching Spotify for `artist='{artist}'` and `song='{song}'`"
            )
            logger.debug(f"Query URL: {query_url}")

            try:
                response = self._session.get(
                    query_url, headers=self.__header, timeout=30
                )
                response.raise_for_status()
            except requests.RequestException as e:
                raise NetworkException(f"Network error occurred: {e}")

            if response.status_code != 200:
                raise SpotifyException(f"Failed to search for music: {response.json()}")

            artist_ids = artist_ids if artist_ids else self._get_artists_ids(artist)
            music_info = self._find_music_info(
                artist, song, response.json(), artist_ids
            )

        return music_info

    def search_advanced(
        self,
        artist: str,
        song: str,
        isrc: str = None,
        upc: str = None,
        limit: int = 1,
        normalize_non_english: bool = True,
    ) -> Optional[MusicInfo]:
        """
        Searches for a song by artist, title, ISRC, or UPC.

        Parameters
        ----------
        artist : str
            The name of the artist.
        song : str
            The title of the song.
        isrc : str, optional
            The ISRC of the track.
        upc : str, optional
            The UPC of the album.
        limit: int, optional
            The number of items to retrieve from API. ``limit >=1 and <= 50``. Default is ``1``.
        normalize_non_english : bool, optional
            Whether to normalize non-English characters for comparison. Default is ``True``.

        Returns
        -------
        Optional[MusicInfo_]
            The music information if found, otherwise None.
        """
        if not is_valid_string(artist) or not is_valid_string(song):
            raise InvalidValueException(
                "Artist and song names must be valid strings and can't be empty."
            )

        self.normalize_non_english = normalize_non_english

        self.__refresh_token_if_expired()

        if isrc:
            query = f"?q={artist} {song} isrc:{isrc}&type=track&limit={limit}"
        elif upc:
            query = f"?q={artist} {song} upc:{upc}&type=album&limit={limit}"
        else:
            raise InvalidValueException("ISRC or UPC must be provided.")

        query_url = f"{self.api_url}/search{query}"
        try:
            response = self._session.get(query_url, headers=self.__header, timeout=30)
            response.raise_for_status()
        except requests.RequestException as e:
            raise NetworkException(f"Network error occurred: {e}")

        if response.status_code != 200:
            raise SpotifyException(
                f"Failed to search music with ISRC/UPC: {response.json()}"
            )

        artist_ids = self._get_artists_ids(artist)
        return self._find_music_info(artist, song, response.json(), artist_ids)

    def _get_artists_ids(self, artist: str) -> Union[list, None]:
        """
        Retrieves the IDs of the artists.

        Parameters
        ----------
        artist : str
            The name of the artist.

        Returns
        -------
        Union[list, None]
            A list of artist IDs or None if not found.
        """
        artist_ids = []
        for name in separate_artists(artist):
            query_url = f"{self.api_url}/search?q={name}&type=artist&limit=5"
            try:
                response = self._session.get(
                    query_url, headers=self.__header, timeout=30
                )
                response.raise_for_status()
            except requests.RequestException as e:
                raise NetworkException(f"Network error occurred: {e}")

            if response.status_code != 200:
                return None

            artist_ids.extend(
                artist["id"] for artist in response.json()["artists"]["items"]
            )
        return artist_ids

    def _find_music_info(
        self, artist: str, song: str, response_json: dict, artist_ids: list
    ) -> Optional[MusicInfo]:
        """
        Finds the music information from the search results.

        Parameters
        ----------
        artist : str
            The name of the artist.
        song : str
            The title of the song.
        response_json : dict
            The JSON response from the API.
        artist_ids : list
            A list of artist IDs.

        Returns
        -------
        Optional[MusicInfo]
            The music information if found, otherwise None.
        """
        try:
            for track in response_json["tracks"]["items"]:
                music_info = self._find_track(song, artist, track, artist_ids)
                if music_info:
                    return music_info
        except KeyError:
            pass

        try:
            for album in response_json["albums"]["items"]:
                music_info = self._find_album(song, artist, album, artist_ids)
                if music_info:
                    return music_info
        except KeyError:
            pass

        logger.warning(
            f"No matching results found for artist='{artist}' and song='{song}'"
        )
        return None

    def _find_track(
        self, song: str, artist: str, track: dict, artist_ids: list
    ) -> Optional[MusicInfo]:
        """
        Finds the track information from the search results.

        Parameters
        ----------
        song : str
            The title of the song.
        artist : str
            The name of the artist.
        track : dict
            A single track from the search results.
        artist_ids : list
            A list of artist IDs.

        Returns
        -------
        Optional[MusicInfo]
            The music information if found, otherwise None.
        """
        if not are_strings_similar(
            track["name"],
            song,
            use_translation=self.normalize_non_english,
            translation_session=self._translation_session,
        ):
            return None

        artists_name = [x["name"] for x in track["artists"]]
        matching_artists = [
            x["name"]
            for x in track["artists"]
            if are_strings_similar(
                x["name"],
                artist,
                use_translation=self.normalize_non_english,
                translation_session=self._translation_session,
            )
            or x["id"] in artist_ids
        ]

        if matching_artists:
            return MusicInfo(
                album_art=track["album"]["images"][0]["url"],
                album_title=track["album"]["name"],
                album_type=track["album"]["album_type"],
                artists=", ".join(artists_name),
                genre=None,
                id=track["id"],
                isrc=track.get("external_ids").get("isrc"),
                lyrics=None,
                release_date=track["album"]["release_date"],
                tempo=None,
                title=track["name"],
                type="track",
                upc=None,
                url=track["external_urls"]["spotify"],
            )

        return None

    def _find_album(
        self, song: str, artist: str, album: dict, artist_ids: list
    ) -> Optional[MusicInfo]:
        """
        Finds the album information from the search results.

        Parameters
        ----------
        song : str
            The title of the song.
        artist : str
            The name of the artist.
        album : dict
            A single album from the search results.
        artist_ids : list
            A list of artist IDs.

        Returns
        -------
        Optional[MusicInfo]
            The music information if found, otherwise None.
        """
        if not are_strings_similar(
            album["name"],
            song,
            use_translation=self.normalize_non_english,
            translation_session=self._translation_session,
        ):
            return None

        artists_name = [x["name"] for x in album["artists"]]
        matching_artists = [
            x["name"]
            for x in album["artists"]
            if are_strings_similar(
                x["name"],
                artist,
                use_translation=self.normalize_non_english,
                translation_session=self._translation_session,
            )
            or x["id"] in artist_ids
        ]

        if matching_artists:
            guess = guess_album_type(album.get("total_tracks", 1))
            guessed_right = are_strings_similar(
                album.get("album_type", "x"), guess, use_translation=False
            )

            return MusicInfo(
                album_art=album["images"][0]["url"],
                album_title=album["name"],
                album_type=album.get("album_type") if guessed_right else guess,
                artists=", ".join(artists_name),
                genre=None,
                id=album["id"],
                isrc=None,
                lyrics=None,
                release_date=album["release_date"],
                tempo=None,
                title=album["name"],
                type=album.get("type"),
                upc=None,
                url=album["external_urls"]["spotify"],
            )

        return None


if __name__ == "__main__":
    import logging

    from yutipy.utils.logger import enable_logging

    enable_logging(level=logging.DEBUG)
    spotify = Spotify(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)

    try:
        artist_name = input("Artist Name: ")
        song_name = input("Song Name: ")
        pprint(spotify.search(artist_name, song_name))
    finally:
        spotify.close_session()
