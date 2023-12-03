from pydantic import BaseModel


class ServerStatus(BaseModel):
    detail: str
