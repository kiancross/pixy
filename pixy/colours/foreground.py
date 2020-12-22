#
# Copyright (c) 2020 Kian Cross
#

from pixy.escape_sequence import EscapeSequence
from pixy.colours import constants

black = EscapeSequence(constants.FOREGROUND_START_CODE + constants.BLACK)
red = EscapeSequence(constants.FOREGROUND_START_CODE + constants.RED)
green = EscapeSequence(constants.FOREGROUND_START_CODE + constants.GREEN)
yellow = EscapeSequence(constants.FOREGROUND_START_CODE + constants.YELLOW)
blue = EscapeSequence(constants.FOREGROUND_START_CODE + constants.BLUE)
magenta = EscapeSequence(constants.FOREGROUND_START_CODE + constants.MAGENTA)
cyan = EscapeSequence(constants.FOREGROUND_START_CODE + constants.CYAN)
white = EscapeSequence(constants.FOREGROUND_START_CODE + constants.WHITE)
