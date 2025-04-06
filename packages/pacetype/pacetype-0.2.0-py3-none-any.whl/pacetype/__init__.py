import sys
from .pacetype import _core_typewrite
import time

__version__ = "0.2.0"

class _PacetypeModule:
    """
    A callable object that replaces the pacetype module,
    allowing direct calling like `pacetype('text', interval)`.
    """
    # Carry over essential module metadata
    __version__ = __version__
    # You might need to explicitly carry over other dunder attributes
    # like __name__, __doc__, __package__, __path__, __file__ if required
    # by other tools or frameworks, although often it's not necessary.
    __all__ = [] # Explicitly define what 'from pacetype import *' would import (nothing)

    def __call__(self, text: str, interval: float = 0.00):
        """
        Types the given text character by character with a specified interval.

        This is the primary function called when using `pacetype(...)`.

        Args:
            text: The string to type.
            interval: The delay in seconds between typing each character.
                      Defaults to 0.00 seconds. Note that a small minimum delay
                      (approx 0.1s) occurs even if interval is set to 0.0,
                      ensuring system reliability.
        """
        # The _core_typewrite function handles the actual typing logic,
        # including the minimum delay enforcement.
        _core_typewrite(text, interval)

# Replace the module object in sys.modules with an instance of our callable class.
# This makes `import pacetype` result in `pacetype` being the callable instance.
sys.modules[__name__] = _PacetypeModule()
