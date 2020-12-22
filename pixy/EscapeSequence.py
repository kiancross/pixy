#
# Copyright (c) 2020 Kian Cross
#


class EscapeSequence(tuple):

    __ESCAPE_CHARACTER = "\x1b"

    def __new__(self, *codes):

        for code in codes:
            if not isinstance(code, int):
                raise TypeError("All codes must be integers.")

        return super().__new__(self, codes)

    def __add__(self, other):
        return EscapeSequence(*super().__add__(other))

    def __str__(self):
        return self.code

    @property
    def code(self):
        return "%s[%sm" % (
            self.__ESCAPE_CHARACTER,
            ";".join(str(code) for code in self),
        )
