from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from config.config_loader import settings
from schema.influencer import InfluencerQuery, InfluencerSchema
from services.authentication import authenticate

router = APIRouter()


@ router.get("/search", response_model=InfluencerSchema, status_code=status.HTTP_200_OK)
async def search_influencer(channel_display_name: str, skip: int = 0, limit: int = 10, token: str = None):
    """ 
    Search and filter a list of influencers with which endpoint.

    Parameters should be sent as url parameters
    """
    if await authenticate(token):
        return JSONResponse(content=f"{settings.DESCRIPTION} Visit /api/v1/docs for more details.",
                            status_code=status.HTTP_200_OK)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")


@ router.get("/search_with_json", response_model=InfluencerSchema, status_code=status.HTTP_200_OK)
async def search_influencer_with_json(influencer_query: InfluencerQuery, token: str = None):
    """ 
    Search and filter a list of influencers with which endpoint.
    Parameters should be sent as json.
    """

    if await authenticate(token):
        return JSONResponse(content=f"{settings.DESCRIPTION} Visit /api/v1/docs for more details.",
                            status_code=status.HTTP_200_OK)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
