from typing import Optional
from pydantic import BaseModel

class MessageBase(BaseModel):
  phone: str
  message: str
  date: str

class Message(MessageBase):
  id: Optional[int] = None

  class Config:
    orm_mode = True