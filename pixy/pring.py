#
# Copyright (c) 2020 Kian Cross
#

from pixy.escape_sequence import EscapeSequence


reset = EscapeSequence(0)


def pring(text: str, style: EscapeSequence = EscapeSequence()) -> str:

    if not isinstance(text, str):
        raise ValueError("text must be of type str")

    if not isinstance(style, EscapeSequence):
        raise ValueError("style must be of type EscapeSequence (or sub-class of).")

    sections = [section for section in text.split(reset.code) if section]

    return style.code + (reset.code + style.code).join(sections) + reset.code
