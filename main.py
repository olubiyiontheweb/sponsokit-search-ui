from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from config.config_loader import settings

# initialize FastAPI
sponsok_search_ui = FastAPI(title=settings.PROJECT_NAME,
                            description=settings.DESCRIPTION,
                            openapi_url=f"{settings.API_V1_STR + settings.OPENAPI_URL}",
                            docs_url=f"{settings.API_V1_STR}/docs",
                            version=settings.VERSION, debug=settings.DEBUG)


@ sponsok_search_ui.get("/")
async def root():
    """ Root route returns simple guide page
    """
    return JSONResponse(content=f'{settings.DESCRIPTION} Visit http://localhost:8000/api/v1/docs for more details.',
                        status_code=status.HTTP_200_OK)
