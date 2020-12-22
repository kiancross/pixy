#
# Copyright (c) 2020 Kian Cross
#

import pytest
import pixy


def test_min_boundary():
    assert isinstance(pixy.Font(0), pixy.Font)

    with pytest.raises(ValueError):
        pixy.Font(-1)


def test_max_boundary():
    assert isinstance(pixy.Font(8), pixy.Font)

    with pytest.raises(ValueError):
        pixy.Font(9)


def test_code():
    font = pixy.Font(5)
    assert font.code == "\x1b[16m"
