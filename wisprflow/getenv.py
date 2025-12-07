from dotenv import load_dotenv
import os
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
load_dotenv(ROOT_DIR / ".env")

def get_env(key: str):
    value = os.getenv(key)
    if not value:
        raise ValueError(f"Missing env variable: {key}")
    return value
