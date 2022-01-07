from typing import List, Optional
from enum import Enum

from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    name: str
    url: str


class VideoFile(BaseModel):
    id: int
    quality: str  # TODO Enum
    file_type: str
    width: Optional[int]
    height: Optional[int]
    link: str


class VideoQuality(str, Enum):
    hd = "hd"
    sd = "sd"
    # NOTE may be more


class VideoPicture(BaseModel):
    id: int
    picture: str
    nr: int


class Video(BaseModel):
    id: int
    width: int
    height: int
    url: str
    image: str
    duration: int
    user: User
    video_files: List[VideoFile]
    video_pictures: List[VideoPicture]
