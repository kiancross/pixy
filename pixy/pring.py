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


reset = EscapeSequence(0)


def pring(text: str, style: EscapeSequence = EscapeSequence()) -> str:

    if not isinstance(text, str):
        raise ValueError("text must be of type str")

    if not isinstance(style, EscapeSequence):
        raise ValueError(
            "style must be of type EscapeSequence (or sub-class of)."
        )

    sections = [section for section in text.split(reset.code) if section]

    return style.code + (reset.code + style.code).join(sections) + reset.code
