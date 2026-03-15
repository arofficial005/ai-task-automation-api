from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="AI Task Automation API")
#app
app.include_router(router)
# home path

#new_lines_denerated

#new_lines_denerated

#new_lines_denerated


@app.get("/")
def health_check():
    return {"status": "running"}
