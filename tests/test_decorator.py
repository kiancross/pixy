#
# Copyright (c) 2020 Kian Cross
#

import pixy


def test_bold():
    assert pixy.decorators.bold.code == "\x1b[1m"

def test_faint():
    assert pixy.decorators.faint.code == "\x1b[2m"

def test_italic():
    assert pixy.decorators.italic.code == "\x1b[3m"

def test_underline():
    assert pixy.decorators.underline.code == "\x1b[4m"

def test_slow_blink():
    assert pixy.decorators.slow_blink.code == "\x1b[5m"

def test_rapid_blink():
    assert pixy.decorators.rapid_blink.code == "\x1b[6m"

def test_invert():
    assert pixy.decorators.invert.code == "\x1b[7m"

def test_conceal():
    assert pixy.decorators.conceal.code == "\x1b[8m"

def test_strike():
    assert pixy.decorators.strike.code == "\x1b[9m"

def test_fraktur():
    assert pixy.decorators.fraktur.code == "\x1b[20m"

def test_double_underline():
    assert pixy.decorators.double_underline.code == "\x1b[21m"

def test_framed():
    assert pixy.decorators.framed.code == "\x1b[51m"

def test_encircled():
    assert pixy.decorators.encircled.code == "\x1b[52m"

def test_overlined():
    assert pixy.decorators.overlined.code == "\x1b[53m"
