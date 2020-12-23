#
# Copyright (c) 2020 Kian Cross
#

from typing import Tuple, Any


class EscapeSequence(Tuple[int]):

    __ESCAPE_CHARACTER = "\x1b"

    def __new__(cls, *codes: int) -> "EscapeSequence":

        for code in codes:
            if not isinstance(code, int):
                raise TypeError("All codes must be integers.")

        return super(EscapeSequence, cls).__new__(cls, codes)  # type: ignore

    def __add__(self, other: Any) -> "EscapeSequence":
        return EscapeSequence(*super().__add__(other))

    def __str__(self) -> str:
        return self.code

    @property
    def code(self) -> str:
        return "%s[%sm" % (
            self.__ESCAPE_CHARACTER,
            ";".join(str(code) for code in self),
        )
