import uvicorn

async def app():
  ...

if __name__ == "__main__":
  uvicorn.run(
    "app.main:app", 
    host="localhost", 
    port=8006,
    reload=True,
    log_level="info",
  )