from fastapi import FastAPI
from app.routers import jobs

app = FastAPI(title="Server Health Monitoring & Automation API")

app.include_router(jobs.router)

@app.get("/")
def root():
    return {"message": "Server Health Monitoring Platform is running."}
