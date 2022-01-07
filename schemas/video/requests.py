from typing import List, Optional
from enum import Enum

from pydantic import BaseModel, Field

from schemas.video.resource import Video


class VideoOrientation(str, Enum):
    landscape = "landscape"
    portrait = "portrait"
    square = "square"


class VideoSearchParams(BaseModel):
    query: str
    orientation: Optional[VideoOrientation]
    size: Optional[str]  # TODO Enum
    locale: Optional[str]  # TODO Enum
    page: Optional[int] = Field(default=1)
    per_page: Optional[int] = Field(default=15, gt=0, le=80)  # 0 < per_page <= 80


class VideoSearchResponse(BaseModel):
    # An array of Video objects:
    videos: List[Video]
    # The Pexels URL for the current search query:
    url: str
    # The current page number:
    page: int
    # The number of results returned with each page:
    per_page: int
    # The total number of results for the request:
    total_results: int
    # URL for the previous page of results, if applicable:
    prev_page: Optional[str]
    # URL for the next page of results, if applicable:
    next_page: Optional[str]


class VideoPopularParams(BaseModel):
    # The minimum width in pixels of the returned videos.
    min_width: Optional[int]
    # The minimum height in pixels of the returned videos.
    min_height: Optional[int]
    # The minimum duration in seconds of the returned videos.
    min_duration: Optional[int]
    # The maximum duration in seconds of the returned videos.
    max_duration: Optional[int]
    # The page number you are requesting. Default: 1
    page: Optional[int] = Field(default=1)
    # The number of results you are requesting per page. Default: 15 Max: 80
    per_page: Optional[int] = Field(default=15, gt=0, le=80)  # 0 < per_page <= 80


class VideoPopularResponse(BaseModel):
    # An array of Video objects:
    videos: List[Video]
    # The Pexels URL for the current search query:
    url: str
    # The current page number:
    page: int
    # The number of results returned with each page:
    per_page: int
    # The total number of results for the request:
    total_results: int
    # URL for the previous page of results, if applicable:
    prev_page: Optional[str]
    # URL for the next page of results, if applicable:
    next_page: Optional[str]
