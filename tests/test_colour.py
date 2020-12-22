#
# Copyright (c) 2020 Kian Cross
#

import pytest
import pixy


def test_black_foreground():
    assert pixy.foreground.black.code == "\x1b[30m"

def test_red_foreground():
    assert pixy.foreground.red.code == "\x1b[31m"

def test_green_foreground():
    assert pixy.foreground.green.code == "\x1b[32m"

def test_yellow_foreground():
    assert pixy.foreground.yellow.code == "\x1b[33m"

def test_blue_foreground():
    assert pixy.foreground.blue.code == "\x1b[34m"

def test_magenta_foreground():
    assert pixy.foreground.magenta.code == "\x1b[35m"

def test_cyan_foreground():
    assert pixy.foreground.cyan.code == "\x1b[36m"

def test_white_foreground():
    assert pixy.foreground.white.code == "\x1b[37m"

def test_black_background():
    assert pixy.background.black.code == "\x1b[40m"

def test_red_background():
    assert pixy.background.red.code == "\x1b[41m"

def test_green_background():
    assert pixy.background.green.code == "\x1b[42m"

def test_yellow_background():
    assert pixy.background.yellow.code == "\x1b[43m"

def test_blue_background():
    assert pixy.background.blue.code == "\x1b[44m"

def test_magenta_background():
    assert pixy.background.magenta.code == "\x1b[45m"

def test_cyan_background():
    assert pixy.background.cyan.code == "\x1b[46m"

def test_white_background():
    assert pixy.background.white.code == "\x1b[47m"

def test_extended_min_boundary():
    assert isinstance(pixy.ExtendedColour(0), pixy.ExtendedColour)

    with pytest.raises(ValueError):
        pixy.ExtendedColour(-1)

def test_extended_max_boundary():
    assert isinstance(pixy.ExtendedColour(255), pixy.ExtendedColour)

    with pytest.raises(ValueError):
        pixy.ExtendedColour(255 + 1)

def test_extended_foreground():
    colour = pixy.ExtendedColour(10)
    assert colour.code == "\x1b[38;5;10m"

def test_extended_background():
    colour = pixy.ExtendedColour(10, True)
    assert colour.code == "\x1b[48;5;10m"

def test_extended_background_named():
    colour = pixy.ExtendedColour(10, background=True)
    assert colour.code == "\x1b[48;5;10m"

def test_true_min_boundary():
    assert isinstance(pixy.TrueColour(0, 0, 0), pixy.TrueColour)

    with pytest.raises(ValueError):
        pixy.TrueColour(-1, 0, 0)

    with pytest.raises(ValueError):
        pixy.TrueColour(0, -1, 0)

    with pytest.raises(ValueError):
        pixy.TrueColour(0, 0, -1)

def test_true_max_boundary():
    assert isinstance(pixy.TrueColour(255, 255, 255), pixy.TrueColour)

    with pytest.raises(ValueError):
        pixy.TrueColour(256, 255, 255)

    with pytest.raises(ValueError):
        pixy.TrueColour(255, 256, 255)

    with pytest.raises(ValueError):
        pixy.TrueColour(255, 255, 256)

def test_true_foreground():
    colour = pixy.TrueColour(10, 20, 30)
    assert colour.code == "\x1b[38;2;10;20;30m"

def test_true_background():
    colour = pixy.TrueColour(10, 20, 30, True)
    assert colour.code == "\x1b[48;2;10;20;30m"

def test_true_background_named():
    colour = pixy.TrueColour(10, 20, 30, background=True)
    assert colour.code == "\x1b[48;2;10;20;30m"
