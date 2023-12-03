from pydantic import BaseModel


class LoginIn(BaseModel):
    nickname: str
    password: str


class LoginOut(BaseModel):
    token: str
    refresh_token: str
    type: str


class RefreshIn(BaseModel):
    refresh_token: str
