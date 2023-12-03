from random import randint
from src.v1.auth import login_required

from database.database import get_session
from database.models import Text
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

text_router = APIRouter()


@text_router.get("/generate")
async def text_generate(tier: int = None,
                        user=Depends(login_required),
                        session: AsyncSession = Depends(get_session)):

    stmt = select(Text)
    
    if tier != None:
        stmt = stmt.where(Text.tier == tier)

    texts = [x[0] for x in (await session.execute(stmt)).all()]

    return texts[randint(0, len(texts)-1)]
