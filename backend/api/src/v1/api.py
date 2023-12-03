from database.database import get_session
from database.models import User
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.v1.auth import auth_router
from src.v1.text import text_router
from src.v1.rating import rating_router
from src.v1.schemas.api import ServerStatus

router = APIRouter()

router.include_router(auth_router, prefix="/auth", tags=["auth"])
router.include_router(text_router, prefix="/text", tags=["text"])
router.include_router(rating_router, prefix="/rating", tags=["rating"])


@router.get("/serverStatus", response_model=ServerStatus, responses={
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
