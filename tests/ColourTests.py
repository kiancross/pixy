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


class ColourTests(unittest.TestCase):

    def test_black_foreground(self):
        self.assertEqual(pixy.foreground.black.code, "\x1b[30m")

    def test_red_foreground(self):
        self.assertEqual(pixy.foreground.red.code, "\x1b[31m")

    def test_green_foreground(self):
        self.assertEqual(pixy.foreground.green.code, "\x1b[32m")

    def test_yellow_foreground(self):
        self.assertEqual(pixy.foreground.yellow.code, "\x1b[33m")

    def test_blue_foreground(self):
        self.assertEqual(pixy.foreground.blue.code, "\x1b[34m")

    def test_magenta_foreground(self):
        self.assertEqual(pixy.foreground.magenta.code, "\x1b[35m")

    def test_cyan_foreground(self):
        self.assertEqual(pixy.foreground.cyan.code, "\x1b[36m")

    def test_white_foreground(self):
        self.assertEqual(pixy.foreground.white.code, "\x1b[37m")

    def test_black_background(self):
        self.assertEqual(pixy.background.black.code, "\x1b[40m")

    def test_red_background(self):
        self.assertEqual(pixy.background.red.code, "\x1b[41m")

    def test_green_background(self):
        self.assertEqual(pixy.background.green.code, "\x1b[42m")

    def test_yellow_background(self):
        self.assertEqual(pixy.background.yellow.code, "\x1b[43m")

    def test_blue_background(self):
        self.assertEqual(pixy.background.blue.code, "\x1b[44m")

    def test_magenta_background(self):
        self.assertEqual(pixy.background.magenta.code, "\x1b[45m")

    def test_cyan_background(self):
        self.assertEqual(pixy.background.cyan.code, "\x1b[46m")

    def test_white_background(self):
        self.assertEqual(pixy.background.white.code, "\x1b[47m")

    def test_extended_min_boundary(self):
        self.assertTrue(isinstance(
            pixy.ExtendedColour(0),
            pixy.ExtendedColour
        ))

        with self.assertRaises(ValueError):
            pixy.ExtendedColour(-1)

    def test_extended_max_boundary(self):
        self.assertTrue(isinstance(
            pixy.ExtendedColour(255),
            pixy.ExtendedColour
        ))

        with self.assertRaises(ValueError):
            pixy.ExtendedColour(255 + 1)

    def test_extended_foreground(self):
        colour = pixy.ExtendedColour(10)
        self.assertEqual(colour.code, "\x1b[38;5;10m")

    def test_extended_background(self):
        colour = pixy.ExtendedColour(10, True)
        self.assertEqual(colour.code, "\x1b[48;5;10m")

    def test_extended_background_named(self):
        colour = pixy.ExtendedColour(10, background=True)
        self.assertEqual(colour.code, "\x1b[48;5;10m")

    def test_true_min_boundary(self):
        self.assertTrue(isinstance(
            pixy.TrueColour(0, 0, 0),
            pixy.TrueColour
        ))

        with self.assertRaises(ValueError):
            pixy.TrueColour(-1, 0, 0)

        with self.assertRaises(ValueError):
            pixy.TrueColour(0, -1, 0)

        with self.assertRaises(ValueError):
            pixy.TrueColour(0, 0, -1)

    def test_true_max_boundary(self):
        self.assertTrue(isinstance(
            pixy.TrueColour(255, 255, 255),
            pixy.TrueColour
        ))

        with self.assertRaises(ValueError):
            pixy.TrueColour(256, 255, 255)

        with self.assertRaises(ValueError):
            pixy.TrueColour(255, 256, 255)

        with self.assertRaises(ValueError):
            pixy.TrueColour(255, 255, 256)

    def test_true_foreground(self):
        colour = pixy.TrueColour(10, 20, 30)
        self.assertEqual(colour.code, "\x1b[38;2;10;20;30m")

    def test_true_background(self):
        colour = pixy.TrueColour(10, 20, 30, True)
        self.assertEqual(colour.code, "\x1b[48;2;10;20;30m")

    def test_true_background_named(self):
        colour = pixy.TrueColour(10, 20, 30, background=True)
        self.assertEqual(colour.code, "\x1b[48;2;10;20;30m")
