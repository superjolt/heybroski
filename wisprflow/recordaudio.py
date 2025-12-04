import sounddevice as sd
import wavio
import numpy as np
import threading
from detectshortcut import detect_shortcut

fs = 44100
channels = 1

# Initialize recording_data as a global list
recording_data = []

def background_recorder():
    global recording_data
    recording = False
    stream = None
    buffer = []

    while True:
        if detect_shortcut():
            if not recording:
                print("Recording started...")
                recording = True
                buffer = []

                # Start a continuous input stream
                stream = sd.InputStream(samplerate=fs, channels=channels, callback=lambda indata, frames, time, status: buffer.append(indata.copy()))
                stream.start()

        else:
            if recording:
                # Stop the stream
                if stream is not None:
                    stream.stop()
                    stream.close()
                stream = None
                print("Recording stopped.")
                recording = False
                if buffer:
                    recording_data.append(np.concatenate(buffer, axis=0))
                    wavio.write
                    print("Saved as shortcut_record.wav")

# Run in a separate thread
thread = threading.Thread(target=background_recorder, daemon=True)
thread.start()