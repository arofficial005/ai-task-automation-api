from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="AI Task Automation API")

app.include_router(router)

@app.get("/")
def health_check():
    return {"status": "running"}
