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


class Font(EscapeSequence):

    __FONT_START_CODE = 11
    __FONT_END_CODE = 19

    def __new__(self, font_number: int):

        number_of_fonts = self.__FONT_END_CODE - self.__FONT_START_CODE

        if font_number < 0 or font_number > number_of_fonts:
            raise ValueError(
                "font must be in-between 0 and %d" % number_of_fonts
            )

        return super().__new__(self, self.__FONT_START_CODE + font_number)
