from __future__ import annotations

import termios
from contextlib import contextmanager
from enum import Enum, auto
from sys import stdin
from typing import TYPE_CHECKING

from quick_key.exceptions import QuickKeyError

if TYPE_CHECKING:
    from collections.abc import Generator


class Key(Enum):
    """
    Possible keypresses to read.
    """

    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
    RETURN = auto()
    SPACE = auto()
    a = auto()
    b = auto()
    c = auto()
    d = auto()
    e = auto()
    f = auto()
    g = auto()
    h = auto()
    i = auto()
    j = auto()
    k = auto()
    l = auto()
    m = auto()
    n = auto()
    o = auto()
    p = auto()
    q = auto()
    r = auto()
    s = auto()
    t = auto()
    u = auto()
    v = auto()
    w = auto()
    x = auto()
    y = auto()
    z = auto()
    n0 = auto()
    n1 = auto()
    n2 = auto()
    n3 = auto()
    n4 = auto()
    n5 = auto()
    n6 = auto()
    n7 = auto()
    n8 = auto()
    n9 = auto()


@contextmanager
def readmode() -> Generator[None]:
    """
    Temporarily change terminal to non-canonical mode with no keypress echoing.
    """
    try:
        old_conf = termios.tcgetattr(stdin.fileno())
        new_conf = termios.tcgetattr(stdin.fileno())
        new_conf[3] &= ~termios.ICANON & ~termios.ECHO & ~termios.C
        termios.tcsetattr(stdin.fileno(), termios.TCSANOW, new_conf)
        yield None
    finally:
        termios.tcsetattr(stdin.fileno(), termios.TCSANOW, old_conf)


def _getch() -> str:
    return stdin.read(1)


def get_key() -> Key:
    """
    Get a keypress.

    Note: Needs to be in a `readmode` context
    """
    match _getch():
        case '\033':
            if _getch() != '[':
                raise QuickKeyError

            match _getch():
                case 'O':
                    match _getch():
                        case 'D':
                            return Key.LEFT
                        case 'C':
                            return Key.RIGHT
                        case 'A':
                            return Key.UP
                        case 'B':
                            return Key.DOWN
                case 'D':
                    return Key.LEFT
                case 'C':
                    return Key.RIGHT
                case 'A':
                    return Key.UP
                case 'B':
                    return Key.DOWN

            raise QuickKeyError

        case '\n':
            return Key.RETURN

        case ' ':
            return Key.SPACE

        case x if x in Key._member_names_:
            return getattr(Key, x)

        case '0':
            return Key.n0
        case '1':
            return Key.n1
        case '2':
            return Key.n2
        case '3':
            return Key.n3
        case '4':
            return Key.n4
        case '5':
            return Key.n5
        case '6':
            return Key.n6
        case '7':
            return Key.n7
        case '8':
            return Key.n8
        case '9':
            return Key.n9

        case _:
            raise QuickKeyError
