import sounddevice
from gtts import gTTS
import os

def speak_it(message, repeat=False): # if the user says "Repeat that?" or something it will repeat the whole sentence slower, thats why slow=repeat 
    audio = gTTS(message, lang="en", slow=repeat, tld="com")
    audio.save("audio.mp3")
    os.system("afplay audio.mp3")
    os.remove("audio.mp3")

speak_it("clash royale")