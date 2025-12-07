import wavio
from wisprflow.askwispr import ask_wispr
from wavtobase64 import wav_to_base64

def process_audio(recording_list, fs):
    if recording_list:
        audio_data = recording_list[-1]
        wavio.write("output.wav", audio_data, fs, sampwidth=2)
        output = wav_to_base64("output.wav")
        ask_wispr(output)
        recording_list.clear()