Python version: 3.10

Virtual environment:
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
# Windows (PowerShell): .venv\Scripts\Activate.ps1

pip install -r requirements.txt

uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000

Expected localhost URL: http://127.0.0.1:8000

FastAPI docs URL: http://127.0.0.1:8000/docs
