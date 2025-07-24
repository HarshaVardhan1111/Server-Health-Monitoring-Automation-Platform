from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import JobLog
import subprocess

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.get("/run-cleanup")
def run_cleanup_job():
    session: Session = SessionLocal()
    try:
        result = subprocess.run(["/bin/bash", "./app/scripts/cleanup.sh"], capture_output=True, text=True)
        status = "success" if result.returncode == 0 else "failed"

        log = JobLog(
            job_name="cleanup",
            status=status,
            stdout=result.stdout,
            stderr=result.stderr
        )
        session.add(log)
        session.commit()

        return {"status": status, "stdout": result.stdout, "stderr": result.stderr}

    except Exception as e:
        return {"status": "error", "detail": str(e)}
    finally:
        session.close()
