from fastapi import APIRouter, HTTPException, Depends

from .controllers import main as main_controller
from .schemas import main as main_schema

router = APIRouter(
  prefix="/messages",
  tags=["messages"],
  responses={404: {"description": "Not found"}}
)

@router.get("/health")
def health():
  return {"messages_is_alive": True}

@router.post("/", response_model=main_schema.Message)
def create_message(
  message: main_schema.MessageBase,
):
  message = main_controller.save_message(message)
  print(message)
  return message