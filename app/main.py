from fastapi import FastAPI
from app.routers import jobs
from app.db import init_db

app = FastAPI(title="Server Health Monitoring & Automation API")

init_db()
app.include_router(jobs.router)

@app.get("/")
def root():
    return {"message": "Server Health Monitoring Platform is running."}
