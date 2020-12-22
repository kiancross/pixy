#
# Copyright (c) 2020 Kian Cross
#

import pytest
import pixy


def test_no_styles():
    assert pixy.pring("foo") == "\x1b[mfoo\x1b[0m"


def test_string_concatonation():

    s = pixy.pring("foo", pixy.foreground.red) + pixy.pring("bar", pixy.foreground.blue)

    assert s == "\x1b[31mfoo\x1b[0m\x1b[34mbar\x1b[0m"


def test_string_concat():

    s1 = pixy.pring("bar", pixy.foreground.red)
    s2 = pixy.pring("foo" + s1, pixy.foreground.blue)

    assert s2 == "\x1b[34mfoo\x1b[31mbar\x1b[0m"


def test_pring_concat():

    s1 = pixy.pring("foo", pixy.foreground.red)
    s2 = pixy.pring("bar", pixy.foreground.blue)
    s3 = pixy.pring(s1 + s2, pixy.decorators.bold)

    assert s3 == "\x1b[1m\x1b[31mfoo\x1b[0m\x1b[1m\x1b[34mbar\x1b[0m"


def test_pring_text_exception():
    with pytest.raises(ValueError):
        pixy.pring(1)


def test_pring_style_exception():
    with pytest.raises(ValueError):
        pixy.pring("foo", 1)
