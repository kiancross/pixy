#
# Copyright (c) 2020 Kian Cross
#

import pytest
import pixy


def test_tuple():
    assert isinstance(pixy.EscapeSequence(1, 2), tuple)


def test_str():
    e = pixy.EscapeSequence(1, 2)
    assert str(e) == e.code


def test_empty():
    assert pixy.EscapeSequence().code == "\x1b[m"


def test_same_add():

    e = pixy.EscapeSequence(1, 2) + pixy.EscapeSequence(3, 4)

    assert isinstance(e, pixy.EscapeSequence)
    assert e == pixy.EscapeSequence(1, 2, 3, 4)
    assert e != pixy.EscapeSequence(1, 2, 3, 4, 5)


def test_extended_colour_add():
    e = pixy.ExtendedColour(10) + pixy.EscapeSequence(3, 4)

    assert isinstance(e, pixy.EscapeSequence)
    assert e == pixy.EscapeSequence(38, 5, 10, 3, 4)


def test_true_colour_add():
    e = pixy.TrueColour(10, 10, 10) + pixy.EscapeSequence(3, 4)

    assert isinstance(e, pixy.EscapeSequence)
    assert e == pixy.EscapeSequence(38, 2, 10, 10, 10, 3, 4)


def test_none_integer():
    with pytest.raises(TypeError):
        pixy.EscapeSequence(10.10)

    with pytest.raises(TypeError):
        pixy.EscapeSequence(10, "hello")
