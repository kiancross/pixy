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

import unittest
import pixy


class AdditionalTests(unittest.TestCase):

    def test_no_styles(self):
        self.assertEqual(pixy.pring("foo"), "\x1b[mfoo\x1b[0m")

    def test_string_concatonation(self):

        s = (pixy.pring("foo", pixy.foreground.red) +
             pixy.pring("bar", pixy.foreground.blue))

        self.assertEqual(s, "\x1b[31mfoo\x1b[0m\x1b[34mbar\x1b[0m")

    def test_string_concat(self):

        s1 = pixy.pring("bar", pixy.foreground.red)
        s2 = pixy.pring("foo" + s1, pixy.foreground.blue)

        self.assertEqual(s2, "\x1b[34mfoo\x1b[31mbar\x1b[0m")

    def test_pring_concat(self):

        s1 = pixy.pring("foo", pixy.foreground.red)
        s2 = pixy.pring("bar", pixy.foreground.blue)
        s3 = pixy.pring(s1 + s2, pixy.decorators.bold)

        self.assertEqual(
            s3,
            "\x1b[1m\x1b[31mfoo\x1b[0m\x1b[1m\x1b[34mbar\x1b[0m"
        )

    def test_pring_text_exception(self):
        with self.assertRaises(ValueError):
            pixy.pring(1)

    def test_pring_style_exception(self):
        with self.assertRaises(ValueError):
            pixy.pring("foo", 1)
