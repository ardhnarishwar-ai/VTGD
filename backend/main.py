from data.option_chain import get_option_chain
from data.live_greeks import parse_greeks
from engine.vtgd_engine import evaluate
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
@app.get("/vtgd/rank")
def vtgd_rank():

    chain = get_option_chain()

    results = []

    for option in chain.get("data", []):

        try:
            g = parse_greeks(option)

            score = evaluate(g)

            results.append({
                "strike": option.get("strikePrice"),
                "type": option.get("optionType"),
                "premium": option.get("ltp"),
                "vtgd": score
            })

        except Exception:
            pass

    return {
        "count": len(results),
        "results": results
    }
