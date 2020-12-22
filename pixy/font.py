#
# Copyright (c) 2020 Kian Cross
#

from pixy.escape_sequence import EscapeSequence


class Font(EscapeSequence):

    __FONT_START_CODE = 11
    __FONT_END_CODE = 19

    def __new__(self, font_number: int):

        number_of_fonts = self.__FONT_END_CODE - self.__FONT_START_CODE

        if font_number < 0 or font_number > number_of_fonts:
            raise ValueError("font must be in-between 0 and %d" % number_of_fonts)

        return super().__new__(self, self.__FONT_START_CODE + font_number)
