from database.database import get_session
from database.models import User
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.api.auth import auth_router
from src.api.schemas.api import ServerStatus

api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth", tags=["auth"])


@api_router.get("/serverStatus", response_model=ServerStatus, responses={
    200: {
        "description": "all working",
        "content": {
            "application/json": {
                "example": {"detail": "server and database are working!"}
            }
        }
    },
    400: {
        "description": "something wrong with connection to database",
        "content": {
            "application/json": {
                "example": {"detail": "connection to the database is corrupted"}
            }
        }
    }
})
async def test(session: AsyncSession = Depends(get_session)):
    try:
        await session.execute(select(User))
        return {"detail": "server and database are working!"}
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=400, detail="connection to the database is corrupted")
