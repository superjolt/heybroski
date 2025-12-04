from speakit import speak_it
from ai.getresponse import get_response

def ask_assistant(message):
    response = get_response(message)
    speak_it(message)