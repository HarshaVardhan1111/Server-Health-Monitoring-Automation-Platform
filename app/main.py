from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.routers import jobs
from app.db import init_db

app = FastAPI(title="Server Health Monitoring API")

init_db()
app.include_router(jobs.router)

# Enable Prometheus metrics
Instrumentator().instrument(app).expose(app)

@app.get("/")
def root():
    return {"message": "Server is healthy"}
