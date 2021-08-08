from typing import Optional
from pydantic import BaseModel
from pydantic.networks import HttpUrl
from datetime import datetime

from pydantic.types import Json


class FollowerCount(BaseModel):
    """
    A follower count
    """
    min_count: int = 1
    max_count: int = 10000


class InfluencerQuery(BaseModel):
    """ 
        Partial schema for querying influencers
    """
    search_text: str = ""
    follower_count: FollowerCount = {
        "min_count": 1,
        "max_count": 10000
    }
    token: str = None


class InfluencerSchema(BaseModel):
    """ 
    Full schema for influencers
    """
    channel_name: str = None
    channel_platform_UID: int = None
    channel_display_name: str = None
    media_count: int = None
    follower_count: int = None
    following_count: int = None
    biography: str = None
    external_url: HttpUrl
    media_url_orig: HttpUrl
    media_url: HttpUrl
    record_time_utc: datetime = None
    data_source: str = None
    category: str = None
    platform: str = None
