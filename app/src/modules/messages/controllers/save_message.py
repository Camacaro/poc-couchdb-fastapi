from turtle import st
from uuid import uuid4
from couchdb import Server
from ..schemas import main as main_schema
from ..helpers import main as main_helpers

def save_message(db: Server, message: main_schema.MessageBase) -> main_schema.MessageTransaction:
  """
  Save a message to the database.
  """
  split1 = message.message.split(". ")

  msgTrans = main_schema.MessageTransaction(
    id=uuid4().hex,
    name=main_helpers.get_name(split1),
    amount=main_helpers.get_amount(split1[0]),
    comprobante=main_helpers.get_referent(split1),
    phone=message.phone,
    details=""
  )

  doc = {
    "_id":msgTrans.id,
    "name":msgTrans.name,
    "amount":msgTrans.amount,
    "comprobante":msgTrans.comprobante,
    "phone":msgTrans.phone,
    "details":msgTrans.details,
  } 

  db.save(doc)
  
  return msgTrans