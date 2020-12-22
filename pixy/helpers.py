#
# Copyright (c) 2020 Kian Cross
#

from pixy.pring import pring
from pixy.colours import foreground


def black(text: str) -> str:
    return pring(text, foreground.black)


def red(text: str) -> str:
    return pring(text, foreground.red)


def green(text: str) -> str:
    return pring(text, foreground.green)


def yellow(text: str) -> str:
    return pring(text, foreground.yellow)


def blue(text: str) -> str:
    return pring(text, foreground.blue)


def magenta(text: str) -> str:
    return pring(text, foreground.magenta)


def cyan(text: str) -> str:
    return pring(text, foreground.cyan)


def white(text: str) -> str:
    return pring(text, foreground.white)
