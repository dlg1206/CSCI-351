"""
File: Status.py
Description: Utility status printer

@author Derek Garcia
"""


class Color:
    """
    Utility class with ASCII color codes
    """
    OK = '\033[92m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'


def valid() -> str:
    """
    :return: "VALID" in bold green
    """
    return f"{Color.BOLD}{Color.OK}VALID{Color.END}"


def invalid() -> str:
    """
    :return: "INVALID" in bold red
    """
    return f"{Color.BOLD}{Color.FAIL}INVALID{Color.END}"
