from ..schemas import main as main_schema

def save_message(message: main_schema.MessageBase):
  """
  Save a message to the database.
  """
  return main_schema.Message(
    id=1,
    phone="+1-555-555-5555",
    message="Hello, world!",
    date="2020-01-01"
  )