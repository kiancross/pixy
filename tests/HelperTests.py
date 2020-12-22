#
# Copyright (c) 2020 Kian Cross
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
