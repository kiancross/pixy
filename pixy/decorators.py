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
