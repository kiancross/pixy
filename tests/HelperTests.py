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


class HelperTests(unittest.TestCase):

    def test_black(self):
        self.assertEqual(pixy.black("foo"), "\x1b[30mfoo\x1b[0m")

    def test_red(self):
        self.assertEqual(pixy.red("foo"), "\x1b[31mfoo\x1b[0m")

    def test_green(self):
        self.assertEqual(pixy.green("foo"), "\x1b[32mfoo\x1b[0m")

    def test_yellow(self):
        self.assertEqual(pixy.yellow("foo"), "\x1b[33mfoo\x1b[0m")

    def test_blue(self):
        self.assertEqual(pixy.blue("foo"), "\x1b[34mfoo\x1b[0m")

    def test_magenta(self):
        self.assertEqual(pixy.magenta("foo"), "\x1b[35mfoo\x1b[0m")

    def test_cyan(self):
        self.assertEqual(pixy.cyan("foo"), "\x1b[36mfoo\x1b[0m")

    def test_white(self):
        self.assertEqual(pixy.white("foo"), "\x1b[37mfoo\x1b[0m")
