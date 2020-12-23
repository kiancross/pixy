#
# Copyright (c) 2020 Kian Cross
#

from typing import cast
from pixy.escape_sequence import EscapeSequence


class Font(EscapeSequence):

    __FONT_START_CODE = 11
    __FONT_END_CODE = 19

    def __new__(cls, font_number: int) -> "Font":

        number_of_fonts = cls.__FONT_END_CODE - cls.__FONT_START_CODE

        if font_number < 0 or font_number > number_of_fonts:
            raise ValueError("font must be in-between 0 and %d" % number_of_fonts)

        return cast(Font, super().__new__(cls, cls.__FONT_START_CODE + font_number))
