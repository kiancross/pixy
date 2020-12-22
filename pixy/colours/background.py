#
# Copyright (c) 2020 Kian Cross
#

from pixy.escape_sequence import EscapeSequence
from pixy.colours import constants

black = EscapeSequence(constants.BACKGROUND_START_CODE + constants.BLACK)
red = EscapeSequence(constants.BACKGROUND_START_CODE + constants.RED)
green = EscapeSequence(constants.BACKGROUND_START_CODE + constants.GREEN)
yellow = EscapeSequence(constants.BACKGROUND_START_CODE + constants.YELLOW)
blue = EscapeSequence(constants.BACKGROUND_START_CODE + constants.BLUE)
magenta = EscapeSequence(constants.BACKGROUND_START_CODE + constants.MAGENTA)
cyan = EscapeSequence(constants.BACKGROUND_START_CODE + constants.CYAN)
white = EscapeSequence(constants.BACKGROUND_START_CODE + constants.WHITE)
