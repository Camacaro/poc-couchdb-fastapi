from fastapi import APIRouter, Depends
from couchdb import Server

from .controllers import main as main_controller
from .schemas import main as main_schema
from ...dependencies import main as main_dependencies

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
  db: Server = Depends(main_dependencies.get_db)
):
  message = main_controller.save_message(db, message)
  return message