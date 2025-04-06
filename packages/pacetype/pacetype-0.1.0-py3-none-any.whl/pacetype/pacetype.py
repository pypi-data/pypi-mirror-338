import pyperclip
import pyautogui
import time
import sys

def typewrite(text: str, interval: float = 0.1):
    """
    Types the given text character by character with a specified interval.

    Uses the clipboard and paste command (Ctrl+V/Cmd+V) for compatibility,
    especially with emojis and special characters.

    Args:
        text: The string to type.
        interval: The delay in seconds between typing each character. Defaults to 0.1.
    """
    if interval < 0:
        raise ValueError("Interval must be non-negative")

    # Determine the paste command based on the platform
    paste_key = 'v'
    if sys.platform == 'darwin': # macOS
        modifier_key = 'command'
    else: # Windows/Linux
        modifier_key = 'ctrl'

    for char in text:
        pyperclip.copy(char)
        # A small delay helps ensure the clipboard is ready before pasting
        # Adjust if necessary for your system speed
        time.sleep(0.05)
        pyautogui.hotkey(modifier_key, paste_key)
        time.sleep(interval)
