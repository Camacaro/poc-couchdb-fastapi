from couchdb import Server 
from ..core import main as core_main
from .get_settings import get_settings

def get_db():
  settings = get_settings()
  print(settings.couchdb_name)
  couch = Server(url=settings.couchdb_host)  
  couch.resource.credentials = (settings.couchdb_name, settings.couchdb_password)

  try:
    db = couch[settings.couchdb_name]
  except:
    db = couch.create(settings.couchdb_name)
  
  return db