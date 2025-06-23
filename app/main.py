from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.router import task
from . import model
from app.database import engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",  # frontend chạy bằng Vite
    "http://127.0.0.1:3000",
    "https://todoapp-typescript-rrh1.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # hoặc ["*"] nếu bạn đang dev
    allow_credentials=True,
    allow_methods=["*"],  # hoặc ["POST", "GET"]
    allow_headers=["*"],
)

app.include_router(task.router)
