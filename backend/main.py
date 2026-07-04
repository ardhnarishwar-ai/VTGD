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
