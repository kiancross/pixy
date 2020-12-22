#
# Copyright (c) 2020 Kian Cross
#

import pixy


def test_black():
    assert pixy.black("foo") == "\x1b[30mfoo\x1b[0m"


def test_red():
    assert pixy.red("foo") == "\x1b[31mfoo\x1b[0m"


def test_green():
    assert pixy.green("foo") == "\x1b[32mfoo\x1b[0m"


def test_yellow():
    assert pixy.yellow("foo") == "\x1b[33mfoo\x1b[0m"


def test_blue():
    assert pixy.blue("foo") == "\x1b[34mfoo\x1b[0m"


def test_magenta():
    assert pixy.magenta("foo") == "\x1b[35mfoo\x1b[0m"


def test_cyan():
    assert pixy.cyan("foo") == "\x1b[36mfoo\x1b[0m"


def test_white():
    assert pixy.white("foo") == "\x1b[37mfoo\x1b[0m"
