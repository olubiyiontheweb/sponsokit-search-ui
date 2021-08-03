from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from config.config_loader import settings

router = APIRouter()


@ router.get("/")
async def root():
    """ Root route returns simple guide page
    """
    return JSONResponse(content=f"{settings.DESCRIPTION} Visit /api/v1/docs for more details.",
                        status_code=status.HTTP_200_OK)
