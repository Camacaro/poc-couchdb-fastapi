import uvicorn
import os
from dotenv import load_dotenv

async def app():
  ...

if __name__ == "__main__":
  load_dotenv()
  
  SERVICE_PORT=os.getenv("SERVICE_PORT")
  SERVICE_HOST=os.environ.get("SERVICE_HOST")
  
  uvicorn.run(
    "app.main:app", 
    host=SERVICE_HOST, 
    port=int(SERVICE_PORT),
    reload=True,
    log_level="info",
  )