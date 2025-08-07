from datetime import datetime, timedelta

from pydantic import EmailStr

from app.core.config import JWT_AUDIENCE, ACCESS_TOKEN_EXPIRE_MINUTES
from app.models.core import CoreModel


class JWTMeta(CoreModel):
    iss: str = 'phresh.io'  # the issuer of the token (that’s us)
    aud: str = JWT_AUDIENCE  # who this token is intended for
    iat: float = datetime.timestamp(datetime.now())  # issued at
    exp: float = datetime.timestamp(datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))  # expires at


class JWTCreds(CoreModel):
    """How we'll identify users"""
    sub: EmailStr
    username: str


class JWTPayload(JWTMeta, JWTCreds):
    """
    JWT Payload right before it's encoded - combine meta and username
    """
    pass


class AccessToken(CoreModel):
    access_token: str
    token_type: str
