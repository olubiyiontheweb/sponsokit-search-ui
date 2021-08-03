from fastapi import FastAPI
from config.config_loader import settings
from routers.all_routers import sponsokit_search_routers, sponsokit_search_index_routers

# initialize FastAPI
sponsokit_search_ui = FastAPI(title=settings.PROJECT_NAME,
                              description=settings.DESCRIPTION,
                              openapi_url=f"{settings.API_V1_STR + settings.OPENAPI_URL}",
                              docs_url=f"{settings.API_V1_STR}/docs",
                              version=settings.VERSION, debug=settings.DEBUG)

sponsokit_search_ui.include_router(sponsokit_search_index_routers)

sponsokit_search_ui.include_router(
    sponsokit_search_routers, prefix=settings.API_V1_STR)
