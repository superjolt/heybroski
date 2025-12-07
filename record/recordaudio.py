import sounddevice as sd
import numpy as np
import threading
import time
from record.detectshortcut import detect_shortcut
from record.processaudio import process_audio
fs = 16000
channels = 1

# Initialize recording_data as a global list
recording_data = []

def background_recorder():
    global recording_data
    recording = False
    stream = None
    buffer = []
    shortcut_released = True  # Track if shortcut was released since last press

    while True:
        if detect_shortcut():
            if not recording and shortcut_released:
                print("Recording started...")
                recording = True
                shortcut_released = False
                buffer = []

                # Start a continuous input stream
                stream = sd.InputStream(samplerate=fs, channels=channels, callback=lambda indata, frames, time, status: buffer.append(indata.copy()))
                stream.start()

        else:
            shortcut_released = True  # Mark shortcut as released
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
                    process_audio(recording_data, fs)
        
        time.sleep(0.1)  # Poll every 100ms instead of continuously
# Run in a separate thread
thread = threading.Thread(target=background_recorder, daemon=True)
thread.start()

# Keep main thread alive
try:
    while True:
        threading.Event().wait(1)
except KeyboardInterrupt:
    print("Exiting...")