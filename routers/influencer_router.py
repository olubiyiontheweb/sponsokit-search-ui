from fastapi import APIRouter, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from config.config_loader import settings
from schema.influencer import InfluencerQuery, InfluencerSchema
from services.authentication import authenticate
from services.elasticsearch_query import elastic_search_query

router = APIRouter()


@ router.get("/search", response_model=InfluencerSchema, status_code=status.HTTP_200_OK)
async def search_influencer(channel_display_name: str, min_follower_count: int = 0, max_follower_count: int = 10000, token: str = None):
    """ 
    Search and filter a list of influencers with this endpoint.

    Parameters should be sent as url parameters
    """
    if authenticate(token):
        influencers = await elastic_search_query.search_influencers(channel_display_name, min_follower_count, max_follower_count)
        return JSONResponse(content=influencers,
                            status_code=status.HTTP_200_OK)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")


@ router.get("/search_with_json", response_model=InfluencerSchema, status_code=status.HTTP_200_OK)
async def search_influencer_with_json(influencer_query: InfluencerQuery):
    """ 
    Search and filter a list of influencers with this endpoint.
    Parameters should be sent as json.
    """
    if authenticate(influencer_query.token):
        influencers = await elastic_search_query.search_influencers(influencer_query.channel_display_name,
                                                                    influencer_query.min_follower_count,
                                                                    influencer_query.max_follower_count)
        return JSONResponse(content=influencers,
                            status_code=status.HTTP_200_OK)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
