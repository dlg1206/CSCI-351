"""
File: Status.py
Description: 

@author Derek Garcia
"""


class Color:
    OK = '\033[92m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'


def valid() -> str:
    return f"{Color.BOLD}{Color.OK}VALID{Color.END}"


def invalid() -> str:
    return f"{Color.BOLD}{Color.FAIL}INVALID{Color.END}"
