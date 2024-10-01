"""Console Color Helpers"""

# David Barnes, Robert Depweg
# CIS 226
# 05-28-23

# System imports
import os

os.system("")  # Required to get the terminal to ALWAYS show colors instead of raw escape codes.


# Decorator to convert Style class to a Singleton
def singleton(cls):
    """Singleton function"""
    return cls()


# Class of different Styles
@singleton
class Style:
    """Contains constants for colors"""

    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"
    CLEAR = "\033[H\033[2J"

    def __getattribute__(self, name):
        """Override default dunder method"""
        value = super().__getattribute__(name)
        print(value, end="")
        return value


def print_x(message):
    """Prints red X in maze output"""
    Style.GREEN  # pylint:disable=W0104
    print(message, end=" ")
    Style.RESET  # pylint:disable=W0104


def print_o(message):
    """Prints green O in maze output"""
    Style.RED  # pylint:disable=W0104
    print(message, end=" ")
    Style.RESET  # pylint:disable=W0104
