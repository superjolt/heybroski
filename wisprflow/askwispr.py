import requests
from .getenv import get_env
from .requestwispr import request_wispr
from ai.askassistant import ask_assistant

def ask_wispr(audio):
    apikey = get_env("wisprflow")
    # session = requests.Session()
    # session.get("https://platform-api.wisprflow.ai/api/v1/dash/warmup_dash")

    # response = request_wispr(session, apikey, audio)
    ask_assistant("hello how are you, and who are you and whats the answer to 3x + 5 = 11")