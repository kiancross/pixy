#
# Copyright (c) 2020 Kian Cross
#

from pixy.escape_sequence import EscapeSequence

bold = EscapeSequence(1)
faint = EscapeSequence(2)
italic = EscapeSequence(3)
underline = EscapeSequence(4)
slow_blink = EscapeSequence(5)
rapid_blink = EscapeSequence(6)
invert = EscapeSequence(7)
conceal = EscapeSequence(8)
strike = EscapeSequence(9)
fraktur = EscapeSequence(20)
double_underline = EscapeSequence(21)
framed = EscapeSequence(51)
encircled = EscapeSequence(52)
overlined = EscapeSequence(53)
