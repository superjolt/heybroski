from pynput import keyboard

# Global flag to track key states
keys_pressed = {"ctrl": False, "shift": False}

def on_press(key):
    try:
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            keys_pressed["ctrl"] = True
        elif key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
            keys_pressed["shift"] = True
    except AttributeError:
        pass

def on_release(key):
    try:
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            keys_pressed["ctrl"] = False
        elif key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
            keys_pressed["shift"] = False
    except AttributeError:
        pass

# Start listener in background
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

def detect_shortcut():
    return keys_pressed["ctrl"] and keys_pressed["shift"]