from fastapi import FastAPI
from src.v1.api import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
    "https://keybattler.poslam.ru",
]

l = [f"http://localhost:{x}" for x in range(0, 65000)]

origins = origins + l

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1")
