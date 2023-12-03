from database.database import get_session
from database.models import Result, Text, Tier, User
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import delete, desc, insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from src.v1.auth import login_required
from src.v1.schemas.rating import RatingIn

rating_router = APIRouter()


@rating_router.post("/add_result")
async def rating_add_result(result: RatingIn,
                            user_in=Depends(login_required),
                            session: AsyncSession = Depends(get_session)):

    text = await session.get(Text, result.text_id)

    if text == None:
        raise HTTPException(status_code=400, detail="text not found")

    user = await session.get(User, result.user_id)

    if user == None:
        raise HTTPException(status_code=400, detail="user not found")

    result_ins = {
        "text_id": result.text_id,
        "user_id": user.id,
        "speed": result.speed,
        "correct_rate": result.correct_rate
    }

    await session.execute(insert(Result).values(result_ins))
    await session.commit()

    return {"detail": "result add success"}


@rating_router.get("/view")
async def rating_add_result(text_id: int = None,
                            tier: int = None,
                            user_in=Depends(login_required),
                            session: AsyncSession = Depends(get_session)):

    if text_id == None and tier == None:

        pass

    elif text_id != None and tier == None:

        users = (await session.execute(select(Result).where(Result.text_id == text_id)))

        result = [x._mapping for x in (await session.execute(
            select(Result.id.label("result_id"),
                   User.nickname,
                   (Tier.speed_ratio*Result.speed +
                    Tier.correct_rate_ratio*Result.correct_rate).label("score"))
            .where(Result.text_id == Text.id)
            .where(Text.tier == Tier.id)
            .where(Result.user_id == User.id)
            .where(Text.id == text_id)
            .order_by(desc("score"))))]

    elif text_id == None and tier != None:

        pass

    else:
        raise HTTPException(status_code=400, detail="wrong parameters")

    return result
