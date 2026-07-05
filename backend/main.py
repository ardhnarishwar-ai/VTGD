from app.auth.smartapi import login
from fastapi import FastAPI

app = FastAPI(
    title="VTGD Backend",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "status": "running",
        "project": "VTGD",
        "message": "VTGD Backend is Live 🚀"
    }
@app.get("/login")
def angel_login():
    smart, session = login()
    return {
        "status": "success",
        "message": "Angel One login successful"
    }


@app.get("/vtgd/demo")
def vtgd_demo():
    return {
        "status": "ready",
        "message": "VTGD Engine Connected"
    }
