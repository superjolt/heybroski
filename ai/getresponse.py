import os
from google import genai
from ai.getenv import get_env

def get_response(aimodel, message):
    geminiapikey=get_env("gemini")
    print("Got the api key")
    client = genai.Client(api_key=geminiapikey)
    print("Got the client, going to generate the response")
    response = client.models.generate_content(
        model=aimodel, contents=message
    )
    print("Response came back. It is:")
    print(response.text)
    return response
