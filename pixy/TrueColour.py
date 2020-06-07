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


class TrueColour(EscapeSequence):

    __MAX_VALUE = 0xFF
    __RGB_SUB_CODE = 2

    def __new__(self, red: int, green: int,
                blue: int, background: bool = False):

        if (min(red, green, blue) < 0 or
                max(red, green, blue) > self.__MAX_VALUE):

            raise ValueError(
                "RGB values must be in-between 0 and %d" % self.__MAX_VALUE
            )

        if background:
            type_code = constants.BACKGROUND_CODE
        else:
            type_code = constants.FOREGROUND_CODE

        return super().__new__(
            self,
            type_code,
            self.__RGB_SUB_CODE,
            red,
            green,
            blue
        )
