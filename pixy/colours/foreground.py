#
# Copyright 2020 Kian Cross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from pixy.EscapeSequence import EscapeSequence
from pixy.colours import constants

black = EscapeSequence(constants.FOREGROUND_START_CODE + constants.BLACK)
red = EscapeSequence(constants.FOREGROUND_START_CODE + constants.RED)
green = EscapeSequence(constants.FOREGROUND_START_CODE + constants.GREEN)
yellow = EscapeSequence(constants.FOREGROUND_START_CODE + constants.YELLOW)
blue = EscapeSequence(constants.FOREGROUND_START_CODE + constants.BLUE)
magenta = EscapeSequence(constants.FOREGROUND_START_CODE + constants.MAGENTA)
cyan = EscapeSequence(constants.FOREGROUND_START_CODE + constants.CYAN)
white = EscapeSequence(constants.FOREGROUND_START_CODE + constants.WHITE)
