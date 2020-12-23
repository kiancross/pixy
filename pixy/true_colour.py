#
# Copyright (c) 2020 Kian Cross
#

from typing import cast
from pixy.escape_sequence import EscapeSequence
from pixy.colours import constants


class TrueColour(EscapeSequence):

    __MAX_VALUE = 0xFF
    __RGB_SUB_CODE = 2

    def __new__(
        cls, red: int, green: int, blue: int, background: bool = False
    ) -> "TrueColour":

        if min(red, green, blue) < 0 or max(red, green, blue) > cls.__MAX_VALUE:

            raise ValueError("RGB values must be in-between 0 and %d" % cls.__MAX_VALUE)

        if background:
            type_code = constants.BACKGROUND_CODE
        else:
            type_code = constants.FOREGROUND_CODE

        return cast(
            TrueColour,
            super().__new__(cls, type_code, cls.__RGB_SUB_CODE, red, green, blue),
        )
