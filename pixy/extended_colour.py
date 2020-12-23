#
# Copyright (c) 2020 Kian Cross
#

from typing import cast
from pixy.escape_sequence import EscapeSequence
from pixy.colours import constants


class ExtendedColour(EscapeSequence):
    def __new__(cls, colour_code: int, background: bool = False) -> "ExtendedColour":

        if colour_code < 0 or colour_code > 255:
            raise ValueError("colour_code must be in-between 0 and 255")

        if background:
            type_code = constants.BACKGROUND_CODE
        else:
            type_code = constants.FOREGROUND_CODE

        return cast(ExtendedColour, super().__new__(cls, type_code, 5, colour_code))
