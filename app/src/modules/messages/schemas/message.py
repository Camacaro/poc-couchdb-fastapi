from typing import Optional
from pydantic import BaseModel

class MessageBase(BaseModel):
  phone: str
  message: str
  date: str

class Message(MessageBase):
  id: Optional[str] = None

  class Config:
    orm_mode = True

class MessageTransaction(BaseModel):
  id: str
  name: str
  phone: str
  comprobante: Optional[str] = None
  amount: str
  details: Optional[str] = None

  class Config:
    orm_mode = True