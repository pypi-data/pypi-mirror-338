# Pacetype 🐢

[![PyPI version](https://badge.fury.io/py/pacetype.svg)](https://badge.fury.io/py/pacetype)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Simulates typing text, including emojis and special characters, with adjustable delays for specific characters. Uses `pyautogui.typewrite()` for speed with standard characters and the clipboard for robust cross-platform compatibility with complex characters (like emojis) that often cause issues with direct key simulation.

## 🤔 Why Pacetype?

Automating keyboard input with libraries like `pyautogui` can be fast for standard text but tricky when dealing with emojis or complex Unicode characters. Direct key simulation (`pyautogui.typewrite`) doesn't always handle these complex characters correctly across different OSs and input methods. Conversely, simulating copy-paste for *every* character is reliable but slower.

`pacetype` offers a hybrid approach:

1.  It detects standard, printable characters and types them rapidly using `pyautogui.typewrite()`.
2.  When it encounters a complex character (emoji, symbol, non-printable), it switches to the clipboard method:
    *   Copies the single complex character to the system clipboard.
    *   Simulates the standard "paste" keyboard shortcut (Ctrl+V or Cmd+V).
    *   Waits for a specified `interval` (if provided) *only after pasting* a complex character.

This hybrid method provides the speed of `typewrite` for normal text and the reliability of the clipboard for special characters.

## 🚀 Installation

```bash
pip install pacetype
```

## ✨ Simple Usage

Using pacetype is straightforward. Just import it and call it directly with the text you want to type.

```python
import pacetype
import time

# Give yourself a moment to switch to the target window
print("Pacetyping in 3 seconds...")
time.sleep(3)

# Type text with complex characters. Delay only applies after 👋 and 🐢.
# Standard characters are typed quickly.
pacetype("Hello World! 👋 Fast standard text. Slow emoji... 🐢", interval=0.5)

# Type text rapidly (no interval delay for clipboard pastes)
pacetype("Typing emojis quickly! ✅🚀", interval=0.0)

# Type standard text very fast (uses typewrite, interval is ignored)
pacetype("This uses pyautogui.typewrite and is fast.", interval=0.5) # interval has no effect here

print("Typing finished!")
```

### Key Points:

*   **Hybrid Typing:** Standard characters are typed using the fast `pyautogui.typewrite(interval=0)`. Complex characters (emojis, etc.) are pasted via the clipboard.
*   **Conditional Delay:** The `interval` argument (defaulting to `0.0`) applies *only* as a `time.sleep()` pause *after* a complex character has been pasted using the clipboard. It does not affect the speed of standard character typing.
*   **Clipboard for Complexity:** The clipboard method ensures greater reliability for emojis and a wide range of special characters that `typewrite` might fail on.

## ⚙️ Features

*   **Hybrid Typing:** Fast typing for standard text, reliable clipboard pasting for complex characters.
*   **Emoji & Unicode Support:** Reliably types emojis and complex characters via the clipboard.
*   **Conditional Delay:** Control paste speed for complex characters with the optional `interval` argument.
*   **Simple Callable API:** Just `import pacetype` and use `pacetype("your text", interval=...)`.
*   **Cross-Platform:** Works on Windows, macOS, and Linux (thanks to `pyperclip` and `pyautogui`).

## ⚠️ Important Notes

*   **Window Focus:** The target application window (e.g., text editor, browser, chat) must have keyboard focus when `pacetype()` is executing.
*   **Clipboard Use:** Pacetype uses the system clipboard when pasting complex characters. Any content you manually copy while it's pasting such a character might be overwritten. The clipboard will contain the last complex character pasted after the script finishes. Standard typing does not affect the clipboard.
*   **Keyboard Shortcuts:** Assumes standard `Ctrl+V` (Windows/Linux) or `Cmd+V` (macOS) paste shortcuts are active.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
