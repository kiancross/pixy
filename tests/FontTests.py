#
# Copyright (c) 2020 Kian Cross
#

import unittest
import pixy


class FontTests(unittest.TestCase):
    def test_min_boundary(self):
        self.assertTrue(isinstance(pixy.Font(0), pixy.Font))

        with self.assertRaises(ValueError):
            pixy.Font(-1)

    def test_max_boundary(self):
        self.assertTrue(isinstance(pixy.Font(8), pixy.Font))

        with self.assertRaises(ValueError):
            pixy.Font(9)

    def test_code(self):
        font = pixy.Font(5)
        self.assertEqual(font.code, "\x1b[16m")
