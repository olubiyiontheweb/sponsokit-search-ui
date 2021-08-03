from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from config.config_loader import settings
from schema.influencer import InfluencerQuery, InfluencerSchema

router = APIRouter()


@ router.get("/search", response_model=InfluencerSchema, status_code=status.HTTP_200_OK)
async def search_influencer(channel_display_name: str, skip: int = 0, limit: int = 10):
    """ 
    Search and filter a list of influencers with which endpoint.
    """
    return JSONResponse(content=f"{settings.DESCRIPTION} Visit /api/v1/docs for more details.",
                        status_code=status.HTTP_200_OK)
