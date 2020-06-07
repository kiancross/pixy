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

class EscapeSequence(tuple):

    __ESCAPE_CHARACTER = '\x1b'

    def __new__(self, *codes):

        for code in codes:
            if not isinstance(code, int):
                raise TypeError("All codes must be integers.")

        return super().__new__(self, codes)

    def __add__(self, other):
        return EscapeSequence(*super().__add__(other))

    def __str__(self):
        return self.code

    @property
    def code(self):
        return "%s[%sm" % (
            self.__ESCAPE_CHARACTER,
            ";".join(str(code) for code in self)
        )
