from fastapi import FastAPI, Depends, Response
from fastapi.middleware.cors import CORSMiddleware

from .src.modules.messages import main as messages_main

app = FastAPI()

origins = [
  "*"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get("/")
def health():
  return {"is_alive": True}

app.include_router(messages_main.router)

