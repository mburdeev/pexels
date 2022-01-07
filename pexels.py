from urllib.parse import urljoin

import requests

from config import API_KEY
from schemas import (
    Video,
    VideoFile,
    VideoOrientation,
    VideoSearchParams,
    VideoSearchResponse,
    VideoPopularParams,
    VideoPopularResponse,
)


class PexelsAPI:

    BASE_API_URL = "https://api.pexels.com/"

    def __init__(self, api_key=API_KEY) -> None:
        self.api_key = api_key

    def get_auth_header(self) -> dict:
        return {"Authorization": self.api_key}

    def search_videos(self, params: "VideoSearchParams"):
        path = "videos/search"
        url = urljoin(PexelsAPI.BASE_API_URL, path)
        headers = self.get_auth_header()
        response = requests.get(url, params=params.dict(), headers=headers)
        # TODO check errors
        response_data = response.json()
        return VideoSearchResponse(**response_data)

    def get_popular_videos(self, params: "VideoPopularParams"):
        path = "videos/popular"
        url = urljoin(PexelsAPI.BASE_API_URL, path)
        headers = self.get_auth_header()
        response = requests.get(url, params=params.dict(), headers=headers)
        # TODO check errors
        response_data = response.json()
        return VideoPopularResponse(**response_data)

    def get_video(self, video_id):
        path = f"videos/videos/{video_id}"
        url = urljoin(PexelsAPI.BASE_API_URL, path)
        headers = self.get_auth_header()
        response = requests.get(url, headers=headers)
        # TODO check errors
        response_data = response.json()
        return Video(**response_data)

    @staticmethod
    def get_format(file_type: str):
        return file_type.split("/")[-1]

    def download_video(self, video: "Video"):
        # TODO get video_file from arg
        video_file: VideoFile = min(
            (video_file for video_file in video.video_files if video_file.width),
            key=lambda video_file: video_file.width,
        )

        video_url = video_file.link
        # TODO check file format
        file_format = self.get_format(video_file.file_type)
        # TODO file name from optional arg
        file_name = f"{video_file.id}.{file_format}"

        response = requests.get(video_url)
        # TODO check response

        # TODO create dir if need
        open(file_name, "wb").write(response.content)

        return file_name


# TODO Use pytest:


def test_search_videos():
    params = VideoSearchParams(query="Ocean", orientation=VideoOrientation.portrait)
    return PexelsAPI().search_videos(params)


def test_get_popular_videos():
    params = VideoPopularParams()
    return PexelsAPI().get_popular_videos(params)


def test_get_video():
    debug_video_id = 1526909
    return PexelsAPI().get_video(debug_video_id)


def test_download_video():
    video = test_get_video()
    return PexelsAPI().download_video(video)
