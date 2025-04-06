# Pacetype 🐢

[![PyPI version](https://badge.fury.io/py/pacetype.svg)](https://badge.fury.io/py/pacetype) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Type text and emojis character-by-character with adjustable delays. A workaround for libraries like PyAutoGUI that struggle with direct emoji input.

## 🤔 Why Pacetype?

Libraries like `pyautogui` are fantastic for automating keyboard input, but they often fail when trying to type emojis or complex Unicode characters directly. This is because they simulate low-level key presses, which don't always map correctly to these characters across different operating systems and input methods.

`pacetype` takes a different approach:

1.  It copies one character (including emojis) at a time to the system clipboard.
2.  It simulates the "paste" keyboard shortcut (Ctrl+V or Cmd+V).
3.  It waits for a specified interval before processing the next character.

This method is generally more reliable for handling a wider range of characters, especially emojis.

## 🚀 Installation

```bash
pip install pacetype
```

## ✨ Usage

```python
import pacetype
import time

# Give yourself a few seconds to switch to the target window
print("Switch to your text editor or chat window in 5 seconds...")
time.sleep(5)

text_to_type = "Hello World! 👋 Typing emojis like 🚀 and ✨ is easy!"
pacetype.typewrite(text_to_type, interval=0.15) # 0.15 seconds between characters

print("\nTyping finished!")
```

## ⚙️ Features

*   **Emoji Support:** Reliably types emojis and complex Unicode characters.
*   **Adjustable Delay:** Control the typing speed with the `interval` parameter.
*   **Simple API:** A single `typewrite` function makes it easy to use.
*   **Cross-Platform (Goal):** Aims to work on Windows, macOS, and Linux (relies on `pyperclip` and `pyautogui`'s cross-platform capabilities).

## ⚠️ Important Notes

*   **Focus:** The script requires the target window (e.g., text editor, browser) to have focus when `pacetype.typewrite()` is running. Make sure you switch to the correct window after starting the script.
*   **Clipboard Interference:** This script heavily uses the clipboard. Anything you copy manually while it's running will be overwritten. The content of the clipboard *after* the script finishes will be the last character typed.
*   **Keyboard Shortcuts:** Relies on standard `Ctrl+V` (Windows/Linux) or `Cmd+V` (macOS) paste shortcuts. If these are remapped on your system, it might not work.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.