import sys
from .pacetype import _core_typewrite
import time

__version__ = "0.3.0" # Updated version reflecting the change

class _PacetypeModule:
    """
    A callable object that replaces the pacetype module,
    allowing direct calling like `pacetype('text', interval)`.
    """
    # Carry over essential module metadata
    __version__ = __version__
    __all__ = [] # Explicitly define what 'from pacetype import *' would import (nothing)

    def __call__(self, text: str, interval: float = 0.00):
        """
        Types the given text using a hybrid approach.

        Uses fast `pyautogui.typewrite` for standard characters and a
        clipboard paste mechanism for complex characters (like emojis)
        that `typewrite` might not handle reliably.

        Args:
            text: The string to type.
            interval: The delay in seconds applied *only* after pasting
                      complex characters via the clipboard. Standard character
                      typing via `typewrite` happens without this specific delay
                      for maximum speed. Defaults to 0.00 seconds.
        """
        # The _core_typewrite function handles the actual typing logic,
        # including the hybrid approach and conditional delay.
        _core_typewrite(text, interval)

# Replace the module object in sys.modules with an instance of our callable class.
# This makes `import pacetype` result in `pacetype` being the callable instance.
sys.modules[__name__] = _PacetypeModule()
