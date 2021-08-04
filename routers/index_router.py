from fastapi import APIRouter, status
from starlette.responses import HTMLResponse
from config.config_loader import settings

router = APIRouter()


@ router.get("/")
async def root():
    """ Root route returns simple guide page
    """
    html_content = """
    <a href="/api/v1/docs">/api/v1/docs</a>
    """
    try:
        return HTMLResponse(content=f"{settings.DESCRIPTION} Visit {html_content} for more details.",
                            status_code=status.HTTP_200_OK)
    except Exception as e:
        return JSONResponse(content=e, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
