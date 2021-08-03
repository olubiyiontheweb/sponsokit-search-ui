from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from config.config_loader import settings
from services.authentication import generate_access_token

router = APIRouter()


@ router.get("/generate_auth_token")
async def generate_auth_token():
    """ Route returns auth token for authenticating API interaction
    """
    return JSONResponse(content={"token": f"{generate_access_token()}"},
                        status_code=status.HTTP_200_OK)
