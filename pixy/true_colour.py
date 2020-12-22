#
# Copyright (c) 2020 Kian Cross
#

from pixy.escape_sequence import EscapeSequence
from pixy.colours import constants


class TrueColour(EscapeSequence):

    __MAX_VALUE = 0xFF
    __RGB_SUB_CODE = 2

    def __new__(self, red: int, green: int, blue: int, background: bool = False):

        if min(red, green, blue) < 0 or max(red, green, blue) > self.__MAX_VALUE:

            raise ValueError(
                "RGB values must be in-between 0 and %d" % self.__MAX_VALUE
            )

        if background:
            type_code = constants.BACKGROUND_CODE
        else:
            type_code = constants.FOREGROUND_CODE

        return super().__new__(self, type_code, self.__RGB_SUB_CODE, red, green, blue)
