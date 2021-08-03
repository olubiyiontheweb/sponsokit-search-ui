import jwt
import datetime
from config.config_loader import settings
from fastapi import HTTPException, status


def generate_access_token():
    payload = {
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7, minutes=60),
        "iat": datetime.datetime.utcnow(),
    }

    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.SESSION_TOKEN_ALGORITHM)


def authenticate(token):
    """ 
    Check if User is logged in
    """
    try:
        if token is None:
            raise HTTPException(detail="Please provide a token to continue",
                                status_code=status.HTTP_401_UNAUTHORIZED)
    except:
        pass

    try:
        jwt.decode(
            jwt=token, key=settings.SECRET_KEY, algorithms=settings.SESSION_TOKEN_ALGORITHM)
        return True
    except jwt.ExpiredSignatureError:
        raise HTTPException(detail="User session has expired. Please login again",
                            status_code=status.HTTP_401_UNAUTHORIZED)
    except jwt.InvalidTokenError:
        raise HTTPException(detail="Invalid token. Please generate a new auth token",
                            status_code=status.HTTP_401_UNAUTHORIZED)
