from gtts import gTTS
import os

def speak_it(message, repeat=False): # if the user says "Repeat that?" or something it will repeat the whole sentence slower, thats why slow=repeat 
    audio = gTTS(message, lang="en", slow=repeat, tld="com")
    print("Got audio from google tts")
    audio.save("audio.mp3")
    print("Saved audio")
    os.system("afplay audio.mp3")
    print("Played audio")
    os.remove("audio.mp3")
    print("Removed audio")