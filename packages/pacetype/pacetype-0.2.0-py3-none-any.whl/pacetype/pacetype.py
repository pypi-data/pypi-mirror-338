import pyperclip
import pyautogui
import time
import sys

def _core_typewrite(text: str, interval: float = 0.0):
    """
    Internal function to type text character by character.

    Uses the clipboard and paste command (Ctrl+V/Cmd+V) for compatibility,
    especially with emojis and special characters.

    Args:
        text: The string to type.
        interval: The delay in seconds between typing each character.
                  Note: The copy/paste operation itself introduces a small,
                  system-dependent delay between characters, even if interval is 0.
    """
    if interval < 0:
        raise ValueError("Interval must be non-negative")

    paste_key = 'v'
    if sys.platform == 'darwin': # macOS
        modifier_key = 'command'
    else: # Windows/Linux
        modifier_key = 'ctrl'

    for char in text:
        pyperclip.copy(char)
        pyautogui.hotkey(modifier_key, paste_key)
        if interval > 0:
            time.sleep(interval)

# Main guard for direct script execution testing.
if __name__ == '__main__':
    print("Testing _core_typewrite directly...")
    print("Pacetyping in 3 seconds...")
    time.sleep(3)
    # Example usage for testing
    _core_typewrite('Hello from Pacetype! 🚀', interval=0.0)
    print("Test complete.")
    