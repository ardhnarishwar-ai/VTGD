from SmartApi import SmartConnect
import pyotp
import os
from typing import Dict, Tuple, Optional

# Environment variable names supported by VTGD
REQUIRED_ENV_VARS = [
    "SMARTAPI_API_KEY",
    "SMARTAPI_CLIENT_CODE",
    "SMARTAPI_MPIN",
    "SMARTAPI_TOTP_SECRET",
]

# Backwards-compatible names (previous naming used in repo)
LEGACY_ENV_MAP = {
    "SMARTAPI_API_KEY": "SMART_API_KEY",
    "SMARTAPI_CLIENT_CODE": "SMART_CLIENT_ID",
    "SMARTAPI_MPIN": "SMART_MPIN",
    "SMARTAPI_TOTP_SECRET": "SMART_TOTP_SECRET",
}


def _resolve_env(name: str) -> Optional[str]:
    """Resolve environment variable using the canonical name, falling back to legacy names if present."""
    val = os.getenv(name)
    if val:
        return val
    legacy = LEGACY_ENV_MAP.get(name)
    if legacy:
        return os.getenv(legacy)
    return None


def get_smartapi_env_status() -> Dict[str, str]:
    """Return a map of required env var -> 'present'|'missing' without revealing values."""
    status = {}
    for k in REQUIRED_ENV_VARS:
        status[k] = "present" if _resolve_env(k) else "missing"
    return status


def create_smartapi() -> SmartConnect:
    """Create SmartConnect using resolved environment API key.

    Raises ValueError if API key is not present.
    """
    api_key = _resolve_env("SMARTAPI_API_KEY")
    if not api_key:
        raise ValueError("SMARTAPI API key not configured in environment")
    return SmartConnect(api_key=api_key)


def login() -> Tuple[Optional[SmartConnect], Optional[dict], Dict[str, str]]:
    """Attempt login using environment variables.

    Returns (smart_client, session_dict, env_status).
    If any required env var is missing, smart_client and session_dict will be None and env_status indicates missing vars.
    """
    env_status = get_smartapi_env_status()
    # If any missing, do not attempt login
    if any(v == "missing" for v in env_status.values()):
        return None, None, env_status

    # Resolve actual values (safe -- we will not print them)
    api_key = _resolve_env("SMARTAPI_API_KEY")
    client_code = _resolve_env("SMARTAPI_CLIENT_CODE")
    mpin = _resolve_env("SMARTAPI_MPIN")
    totp_secret = _resolve_env("SMARTAPI_TOTP_SECRET")

    try:
        smart = SmartConnect(api_key=api_key)
        # Generate TOTP code -- library pyotp used in repo
        totp = pyotp.TOTP(totp_secret).now()

        session = smart.generateSession(
            client_code,
            mpin,
            totp
        )
        return smart, session, env_status
    except Exception as e:
        # Do not expose secrets or sensitive internals in exception output
        # Return None for smart/session and include an error entry in env_status
        env_status["error"] = str(e)
        return None, None, env_status
