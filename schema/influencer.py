from pydantic import BaseModel
from pydantic.networks import HttpUrl
from datetime import datetime


class InfluencerQuery(BaseModel):
    """ 
        Partial schema for querying influencers
    """
    channel_display_name: str = None
    follower_count: int = None


class InfluencerSchema(InfluencerQuery):
    """ 
    Full schema for influencers
    """
    channel_name: str = None
    channel_platform_UID: int = None
    media_count: int = None
    following_count: int = None
    biography: str = None
    external_url: HttpUrl
    media_url_orig: HttpUrl
    media_url: HttpUrl
    record_time_utc: datetime = None
    data_source: str = None
    category: str = None
    platform: str = None
