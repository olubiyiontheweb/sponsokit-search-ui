from typing import List, Optional
from fastapi import APIRouter, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic.types import PositiveInt
from config.config_loader import settings
from schema.influencer import InfluencerQuery, InfluencerSchema, FollowerCount
from services.authentication import authenticate
from services.elasticsearch_query import elastic_search_query

router = APIRouter()


@ router.post("/search/{page_no}", response_model=List[InfluencerSchema])
async def search_influencer(page_no: PositiveInt = 1, token: str = None, search_text: str = None, min_follower_count: int = 0, max_follower_count: int = 10000):
    """
    Search and filter a list of influencers with this endpoint.

    Parameters should be sent as url parameters
    """
    if token is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Authentication token required")

    try:
        if authenticate(token):
            influencers = await elastic_search_query.search_influencers(search_text, min_follower_count, max_follower_count, page_no)
            return JSONResponse(content=influencers,
                                status_code=status.HTTP_200_OK)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@ router.post("/search_with_json/{page_no}", response_model=List[InfluencerSchema])
async def search_influencer_with_json(influencer_query: InfluencerQuery, page_no: PositiveInt = 1):
    """
    Search and filter a list of influencers with this endpoint.
    Parameters should be sent as json.
    """
    # clean request data

    if influencer_query.token is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Authentication token required")

    try:
        influencer_query = influencer_query.dict(
            exclude_unset=True, exclude_none=True)
        influencer_query = jsonable_encoder(
            InfluencerQuery(**influencer_query))
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    try:
        if authenticate(influencer_query["token"]):
            influencers = await elastic_search_query.search_influencers(influencer_query["search_text"],
                                                                        influencer_query["follower_count"]["min_count"],
                                                                        influencer_query["follower_count"]["max_count"], page_no)
            return JSONResponse(content=influencers,
                                status_code=status.HTTP_200_OK)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Not authenticated {str(e)}")
