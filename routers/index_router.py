from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from config.config_loader import settings

router = APIRouter()


@ router.get("/")
async def root():
    """ Root route returns simple guide page
    """
    try:
        return JSONResponse(content=f"{settings.DESCRIPTION} Visit /api/v1/docs for more details.",
                            status_code=status.HTTP_200_OK)
    except Exception as e:
        return JSONResponse(content=e, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
