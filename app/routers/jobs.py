from fastapi import APIRouter
import subprocess

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.get("/run-cleanup")
def run_cleanup_job():
    try:
        result = subprocess.run(["/bin/bash", "./app/scripts/cleanup.sh"], capture_output=True, text=True)
        return {
            "status": "success" if result.returncode == 0 else "failed",
            "stdout": result.stdout,
            "stderr": result.stderr
        }
    except Exception as e:
        return {"status": "error", "detail": str(e)}
