from datetime import datetime, timedelta

from config import (
    ALGORITHM,
    AUTH_TOKEN_LIFE,
    REFRESH_TOKEN_LIFE,
    RT_SECRET,
    SECRET_AUTH,
)
from database.database import get_session
from database.models import RefreshTokenStorage, User
from fastapi import APIRouter, Depends, Header, HTTPException
from jwt import decode, encode
from sqlalchemy import delete, insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from src.v1.schemas.auth import LoginIn, LoginOut, RefreshIn
from src.utils import time
from werkzeug.security import check_password_hash, generate_password_hash

auth_router = APIRouter()


async def type_required(
    types: list, auth: str = Header(None), session: AsyncSession = Depends(get_session)
):
    data = None
    try:
        data = decode(auth, SECRET_AUTH, algorithms=[ALGORITHM])

        token_expired_time = datetime.strptime(data["expired"], "%Y-%m-%d %H:%M:%S.%f")

        if token_expired_time < time():
            raise Exception

    except:
        raise HTTPException(status_code=401, detail="token is invalid")

    user = await session.get(User, data["id"])

    if user == None:
        raise HTTPException(status_code=400, detail="user not found")

    if types != []:
        if user.type.name not in types:
            raise HTTPException(status_code=400, detail="not allowed")

    return user


async def login_required(
    auth: str = Header(None), session: AsyncSession = Depends(get_session)
):
    return await type_required(["client"], auth, session)


async def moderator_required(
    auth: str = Header(None), session: AsyncSession = Depends(get_session)
):
    return await type_required(["moderator"], auth, session)


def make_token(user_id: int):
    return encode(
        {"id": user_id, "expired": str(time() + timedelta(days=int(AUTH_TOKEN_LIFE)))},
        SECRET_AUTH,
    )


def make_refresh_token(user_id: int):
    return encode(
        {
            "id": user_id,
            "expired": str(time() + timedelta(days=int(REFRESH_TOKEN_LIFE))),
        },
        RT_SECRET,
    )


@auth_router.post(
    "/login",
    response_model=LoginOut,
    responses={
        200: {
            "description": "success",
            "content": {
                "application/json": {
                    "example": {
                        "token": "string",
                        "refresh_token": "string",
                        "type": "moderator",
                    }
                }
            },
        }
    },
)
async def login_func(data: LoginIn, session: AsyncSession = Depends(get_session)):
    nickname = data.nickname.lstrip(" ").rstrip(" ")
    password = data.password.lstrip(" ").rstrip(" ")

    user = (
        await session.execute(select(User).where(User.nickname == nickname))
    ).first()

    if user == None:
        raise HTTPException(status_code=404, detail="wrong auth data")

    user: User = user[0]

    if not check_password_hash(user.password, password):
        raise HTTPException(status_code=404, detail="wrong auth data")

    token = make_token(user.id)
    refresh_token = make_refresh_token(user.id)

    return {"token": token, "refresh_token": refresh_token, "type": user.type.name}


@auth_router.post(
    "/refresh",
    response_model=LoginOut,
    responses={
        200: {
            "description": "success",
            "content": {
                "application/json": {
                    "example": {
                        "token": "string",
                        "refresh_token": "string",
                        "type": "moderator",
                    }
                }
            },
        },
        400: {
            "description": "incorrect token",
            "content": {
                "application/json": {"example": {"detail": "token is invalid"}}
            },
        },
        404: {
            "description": "no user by that token",
            "content": {"application/json": {"example": {"detail": "user not found"}}},
        },
    },
)
async def refresh(data: RefreshIn, session: AsyncSession = Depends(get_session)):
    refresh_token_recieved = data.refresh_token

    try:
        token_data = decode(refresh_token_recieved, RT_SECRET, algorithms=[ALGORITHM])

        token_expired_time = datetime.strptime(
            token_data["expired"], "%Y-%m-%d %H:%M:%S.%f"
        )

        if token_expired_time < time():
            raise Exception

    except:
        raise HTTPException(status_code=400, detail="token is invalid")

    tokens = (
        await session.execute(
            select(
                RefreshTokenStorage.id,
                RefreshTokenStorage.refresh_token,
                RefreshTokenStorage.expired,
            )
        )
    ).all()

    for token in tokens:
        token = token._mapping

        if token["expired"] < time():
            await session.execute(
                delete(RefreshTokenStorage).where(RefreshTokenStorage.id == token["id"])
            )
            await session.commit()

        if token["refresh_token"] == refresh_token_recieved:
            raise HTTPException(status_code=400, detail="token is invalid")

    user_id = token_data["id"]

    user = await session.get(User, user_id)

    if user == None:
        raise HTTPException(status_code=404, detail="user not found")

    token = make_token(user_id)

    refresh_token = make_refresh_token(user_id)

    user_type = (await session.get(User, user_id)).type.name

    await session.execute(
        insert(RefreshTokenStorage).values(
            {"refresh_token": refresh_token_recieved, "expired": token_expired_time}
        )
    )

    await session.commit()

    return {"token": token, "refresh_token": refresh_token, "type": user_type}


@auth_router.post(
    "/signup",
    responses={
        200: {
            "description": "success",
            "content": {
                "application/json": {"example": {"detail": "successfully registered"}}
            },
        },
        400: {
            "description": "nickname is already in use",
            "content": {
                "application/json": {"example": {"detail": "nickname already picked"}}
            },
        },
    },
)
async def signup(data: LoginIn, session: AsyncSession = Depends(get_session)):
    nickname = data.nickname.lstrip(" ").rstrip(" ")
    password = data.password.lstrip(" ").rstrip(" ")

    user = (
        await session.execute(select(User).where(User.nickname == nickname))
    ).first()

    if user != None:
        raise HTTPException(status_code=400, detail="nickname already picked")

    user = {
        "nickname": nickname,
        "password": generate_password_hash(password),
    }

    await session.execute(insert(User).values(user))
    await session.commit()

    return {"detail": "successfully registered"}
