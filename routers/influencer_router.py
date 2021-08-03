from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from config.config_loader import settings
from schema.influencer import InfluencerQuery, InfluencerSchema
from services.authentication import authenticate

router = APIRouter()


@ router.get("/search", response_model=InfluencerSchema, status_code=status.HTTP_200_OK)
async def search_influencer(channel_display_name: str, skip: int = 0, limit: int = 10):
    """ 
    Search and filter a list of influencers with which endpoint.

    Parameters on the path are interpreted as query parameters
    """
    return JSONResponse(content=f"{settings.DESCRIPTION} Visit /api/v1/docs for more details.",
                        status_code=status.HTTP_200_OK)


@ router.get("/search_with_json", response_model=InfluencerSchema, status_code=status.HTTP_200_OK)
async def search_influencer_with_json(influencer_query: InfluencerQuery):
    """ 
    Search and filter a list of influencers with which endpoint.
    Parameters should be set as json.
    """

    if authenticate:
        pass

    return JSONResponse(content=f"{settings.DESCRIPTION} Visit /api/v1/docs for more details.",
                        status_code=status.HTTP_200_OK)
