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

from pixy.pring import pring
from pixy.colours import foreground


def black(text: str) -> str:
    return pring(text, foreground.black)


def red(text: str) -> str:
    return pring(text, foreground.red)


def green(text: str) -> str:
    return pring(text, foreground.green)


def yellow(text: str) -> str:
    return pring(text, foreground.yellow)


def blue(text: str) -> str:
    return pring(text, foreground.blue)


def magenta(text: str) -> str:
    return pring(text, foreground.magenta)


def cyan(text: str) -> str:
    return pring(text, foreground.cyan)


def white(text: str) -> str:
    return pring(text, foreground.white)
