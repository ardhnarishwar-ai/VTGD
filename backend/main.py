from app.ws.live_feed import start_live_feed
from data.cache import TickCache
from data.option_chain import get_option_chain
from data.live_greeks import parse_greeks
from engine.vtgd_engine import evaluate
from app.auth.smartapi import login, get_smartapi_env_status
from fastapi import FastAPI

app = FastAPI(
    title="VTGD Backend",
    version="1.0.0"
)

@app.on_event("startup")
def startup():
    return
    # start_live_feed()

cache = TickCache()

@app.get("/")
def home():
    return {
        "status": "running",
        "project": "VTGD",
        "message": "VTGD Backend is Live 🚀"
    }


@app.get("/env")
def env_status():
    """Return presence status of required SMARTAPI_* environment variables without revealing values."""
    return get_smartapi_env_status()

@app.get("/login")
def angel_login():
    smart, session, env = login()

    if any(v == "missing" for v in env.values()):
        return {
            "status": "error",
            "message": "Missing SMARTAPI environment variables",
            "env": env
        }

    if smart is None or session is None:
        return {
            "status": "error",
            "message": "Login failed",
            "env": env
        }

    return {
        "status": "success",
        "session": session,
        "env": env
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
            # Parse option into VTGD Greeks object
            g = parse_greeks(option)

            # Evaluate VTGD engine for this option
            vtgd_result = evaluate(g) or {}

            # Ensure net_weight and safety exist (these are provided by evaluate)
            net_w = vtgd_result.get("net_weight")
            safety_v = vtgd_result.get("safety")

            # Extract PCR and FVP from option payload if available; preserve research if absent
            # (do NOT compute PCR or FVP here; just map existing payload fields)
            pcr_val = option.get("pcr") or option.get("PCR") or option.get("pcrValue") or None
            fvp_val = option.get("vwap") or option.get("fvp") or option.get("fairValue") or None

            # Build the result entry (preserve original option metadata and engine outputs)
            entry = {
                "symbol": option.get("symbol") or option.get("name"),
                "strike": option.get("strikePrice") or option.get("strike") or option.get("strike_price"),
                "type": option.get("optionType") or option.get("type") or option.get("instrumentType"),
                "premium": float(option.get("ltp") or option.get("lastPrice") or 0.0),
                "vtgd": {
                    "net_weight": net_w,
                    "safety": safety_v,
                    # strike_rank and diffusion remain as returned by evaluate
                    "strike_rank": vtgd_result.get("strike_rank"),
                    "diffusion": vtgd_result.get("diffusion"),
                    # Map PCR & FVP from payload when available; otherwise null (explicit)
                    "pcr": pcr_val,
                    "fvp": fvp_val
                },
                # preserve raw greeks mapping for debug/trace (optional)
                "raw": option
            }

            results.append(entry)

        except Exception:
            # preserve existing behavior but avoid silent failures in sorting/response
            # Optionally log the exception here in real deployment
            continue

    results.sort(
        key=lambda x: (x.get("vtgd") or {}).get("strike_rank") or 0,
        reverse=True
    )

    return {
        "count": len(results),
        "top_ce": next((x for x in results if x["type"] == "CE"), None),
        "top_pe": next((x for x in results if x["type"] == "PE"), None),
        "results": results
    }

@app.get("/vtgd/top")
def vtgd_top():

    ranking = vtgd_rank()

    return {
        "best_call": ranking["top_ce"],
        "best_put": ranking["top_pe"]
    }
@app.get("/vtgd/cache")
def vtgd_cache():

    return {
        "symbols": list(cache.previous.keys()),
        "count": len(cache.previous)
    }
@app.get("/option-test")
def option_test():

    data = get_option_chain(
        exchange="NFO",
        symbol="NIFTY"
    )

    return data
