from fastapi import APIRouter
from routers import index_router, influencer_router, auth_token


# routers for Sponsokit platform

sponsokit_search_routers = APIRouter()
sponsokit_search_index_routers = APIRouter()

# these are sponsosearch endpoints
sponsokit_search_index_routers.include_router(
    index_router.router, tags=["Index"])
sponsokit_search_routers.include_router(
    auth_token.router, tags=["Generate Auth Token"])
sponsokit_search_routers.include_router(
    influencer_router.router, tags=["Influencer Search"])
