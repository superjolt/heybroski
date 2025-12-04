import keyboard

def detect_shortcut():
    return keyboard.is_pressed('ctrl') and keyboard.is_pressed('shift')