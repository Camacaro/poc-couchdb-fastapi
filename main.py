import os
from fastapi import FastAPI
from couchdb import Server   # importing couchdb  
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

COUCHDB_NAME=os.getenv("COUCHDB_NAME")
COUCHDB_PASSWORD=os.getenv("COUCHDB_PASSWORD")
COUCHDB_HOST=os.getenv("COUCHDB_HOST")

app = FastAPI()

@app.get("/")
async def root():
  # Connecting with couchdb Server   
  couch = Server(url=COUCHDB_HOST)  
  couch.resource.credentials = (COUCHDB_NAME, COUCHDB_PASSWORD)
  # Creating Database  
  # db = couch.create('poccouchdb') 
  # Get Database
  db = couch['poccouchdb']
  doc = {'name':'Employee'}  
  # Creating document  
  doc = {'name':'Employee2'}  
  db.save(doc) # Saving document 
  # Fetching document from the database  
  getName = doc['name'] 
  return {"message": getName}