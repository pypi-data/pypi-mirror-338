import pyperclip
import pyautogui
import time
import sys
import unicodedata

def _is_complex_char(char):
    """
    Checks if a character is likely to cause issues with direct typewrite.
    Focuses on emojis and complex symbols.
    A more robust check might be needed depending on observed issues.
    """
    # Basic check: Treat anything outside basic printable ASCII + extended latin as potentially complex.
    # Also check Unicode category for symbols/emojis.
    if not char.isprintable():
        return True
    try:
        # Check if it's in ranges often used for emojis/symbols
        if 0x1F300 <= ord(char) <= 0x1F5FF or \
           0x1F600 <= ord(char) <= 0x1F64F or \
           0x1F680 <= ord(char) <= 0x1F6FF or \
           0x2600 <= ord(char) <= 0x26FF or \
           0x2700 <= ord(char) <= 0x27BF or \
           0xFE00 <= ord(char) <= 0xFE0F or \
           0x1FA70 <= ord(char) <= 0x1FAFF:
           return True
        # Check unicode category
        category = unicodedata.category(char)
        if category.startswith('S') or category.startswith('Z'): # Symbol or Separator (includes spaces, but typewrite handles them)
             # Allow space through typewrite
             if char == ' ':
                 return False
             # Consider other symbols/separators complex for now
             # This might be too broad, refinement may be needed.
             # return True # Temporarily disabling broad symbol check, focusing on emojis
             pass

    except ValueError:
        # Likely a multi-byte character pyautogui might struggle with
        return True

    # If none of the above, assume typewrite can handle it.
    return False


def _core_typewrite(text: str, interval: float = 0.0):
    """
    Internal function to type text using a hybrid approach.

    Uses pyautogui.typewrite for sequences of standard characters
    and the clipboard/paste method for complex characters (like emojis)
    that typewrite might not handle reliably.

    Args:
        text: The string to type.
        interval: The delay in seconds *only* applied after pasting
                  complex characters via the clipboard. Standard character
                  typing via typewrite happens without this delay.
    """
    if interval < 0:
        raise ValueError("Interval must be non-negative")

    paste_key = 'v'
    if sys.platform == 'darwin': # macOS
        modifier_key = 'command'
    else: # Windows/Linux
        modifier_key = 'ctrl'

    current_chunk = ""
    for char in text:
        if _is_complex_char(char):
            # If we have a pending chunk of simple characters, type it first
            if current_chunk:
                pyautogui.typewrite(current_chunk, interval=0)
                current_chunk = ""

            # Handle the complex character using clipboard
            pyperclip.copy(char)
            pyautogui.hotkey(modifier_key, paste_key)
            # Apply interval delay ONLY after clipboard paste
            if interval > 0:
                time.sleep(interval)
        else:
            # Append simple character to the current chunk
            current_chunk += char

    # Type any remaining simple characters chunk
    if current_chunk:
        pyautogui.typewrite(current_chunk, interval=0)


# Main guard for direct script execution testing.
if __name__ == '__main__':
    print("Testing _core_typewrite directly...")
    print("Pacetyping in 3 seconds...")
    time.sleep(3)
    test_string = "Hello World! 👋 This is a test 🐢 with emojis and standard text."
    print(f"Typing: {test_string}")
    _core_typewrite(test_string, interval=0.1) # Use a small interval for testing complex chars
    print("\nTest complete.")
    print("Testing fast typing (interval=0.0)...")
    time.sleep(3)
    _core_typewrite("Fast typing without emojis.", interval=0.0)
    print("\nFast typing test complete.")
