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
                            user=Depends(login_required),
                            session: AsyncSession = Depends(get_session)):

    text = await session.get(Text, result.text_id)

    if text == None:
        raise HTTPException(status_code=400, detail="text not found")

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

    result = []
    
    try:
        if text_id == None and tier == None:

            users = (await session.execute(select(User.id)))

            for user_raw in users:

                user_id = user_raw._mapping["id"]

                result.append([x._mapping for x in (await session.execute(
                    select(Result.id.label("result_id"),
                        User.nickname,
                        Text.id.label("text_id"),
                        Result.speed,
                        Result.correct_rate,
                        (Tier.speed_ratio*Result.speed +
                            Tier.correct_rate_ratio*Result.correct_rate).label("score"))
                    .where(Result.text_id == Text.id)
                    .where(Text.tier == Tier.id)
                    .where(Result.user_id == User.id)
                    .where(Result.user_id == user_id)
                    .order_by(desc("score"))))][0])

        elif text_id != None and tier == None:

            users = (await session.execute(select(Result.user_id).where(Result.text_id == text_id))).unique().all()

            for user_raw in users:

                user_id = user_raw._mapping["user_id"]

                result.append([x._mapping for x in (await session.execute(
                    select(Result.id.label("result_id"),
                        User.nickname,
                        Result.speed,
                        Result.correct_rate,
                        (Tier.speed_ratio*Result.speed +
                            Tier.correct_rate_ratio*Result.correct_rate).label("score"))
                    .where(Result.text_id == Text.id)
                    .where(Text.tier == Tier.id)
                    .where(Result.user_id == User.id)
                    .where(Result.user_id == user_id)
                    .where(Text.id == text_id)
                    .order_by(desc("score"))))][0])

        elif text_id == None and tier != None:

            users = (await session.execute(select(Result.user_id)
                                        .where(Result.text_id == Text.id)
                                        .where(Text.tier == Tier.id)
                                        .where(Tier.id == tier))).unique().all()

            for user_raw in users:

                user_id = user_raw._mapping["user_id"]

                result.append([x._mapping for x in (await session.execute(
                    select(Result.id.label("result_id"),
                        User.nickname,
                        Text.id.label("text_id"),
                        Result.speed,
                        Result.correct_rate,
                        (Tier.speed_ratio*Result.speed +
                            Tier.correct_rate_ratio*Result.correct_rate).label("score"))
                    .where(Result.text_id == Text.id)
                    .where(Text.tier == Tier.id)
                    .where(Tier.id == tier)
                    .where(Result.user_id == User.id)
                    .where(Result.user_id == user_id)
                    .order_by(desc("score"))))][0])

        else:
            raise HTTPException(status_code=400, detail="wrong parameters")
        
    except:
        return result
