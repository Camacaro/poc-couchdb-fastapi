from turtle import st
from uuid import uuid4
from couchdb import Server
from ..schemas import main as main_schema

def save_message(db: Server, message: main_schema.MessageBase):
  """
  Save a message to the database.
  """
  msg = main_schema.Message(
    id=uuid4().hex,
    phone=message.phone,
    message=message.message,
    date=message.date
  )

  doc = {
    "_id": msg.id,
    "phone": msg.phone,
    "message": msg.message,
    "date": msg.date,
  } 

  db.save(doc)
  
  return msg