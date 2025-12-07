from .speakit import speak_it
from ai.getresponse import get_response
from ai.chathistory import get_chat_history
from ai.chathistory import add_to_chat_history

def ask_assistant(message):
    instructions = "You are a helpful AI assistant named 'Broski'." \
    "Your message should not contain any special characters, your output will be hooked up to Google TTS, and will pronounce those special characters wrong." \
    "Keep it as plain and short as you can. With maxmimum 50 words of response. The user speaks to you, the user does not type. The user tries to have a conversation" \
    "So keep it as if you are having a conversation." \
    "This is the chat history. You have been talking to the user before, you just don't remember. This is what you were talking about."

    chat_history = get_chat_history()

    prompt = instructions + "\n\n" + chat_history + "\n\n" + message
    response = get_response("gemini-2.5-flash", prompt)

    add_to_chat_history(message, response)
    
    speak_it(response.text)