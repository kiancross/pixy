#
# Copyright (c) 2020 Kian Cross
#

import unittest
import pixy


class EscapeSequenceTests(unittest.TestCase):
    def test_tuple(self):
        self.assertTrue(isinstance(pixy.EscapeSequence(1, 2), tuple))

    def test_empty(self):
        self.assertTrue(pixy.EscapeSequence().code, "\x1b[m")

    def test_same_add(self):

        e = pixy.EscapeSequence(1, 2) + pixy.EscapeSequence(3, 4)

        self.assertTrue(isinstance(e, pixy.EscapeSequence))
        self.assertEqual(e, pixy.EscapeSequence(1, 2, 3, 4))
        self.assertNotEqual(e, pixy.EscapeSequence(1, 2, 3, 4, 5))

    def test_extended_colour_add(self):
        e = pixy.ExtendedColour(10) + pixy.EscapeSequence(3, 4)

        self.assertTrue(isinstance(e, pixy.EscapeSequence))
        self.assertTrue(e.code, pixy.EscapeSequence(38, 5, 10, 3, 4))

    def test_true_colour_add(self):
        e = pixy.TrueColour(10, 10, 10) + pixy.EscapeSequence(3, 4)

        self.assertTrue(isinstance(e, pixy.EscapeSequence))
        self.assertTrue(e.code, pixy.EscapeSequence(38, 2, 10, 10, 10, 3, 4))

    def test_none_integer(self):
        with self.assertRaises(TypeError):
            pixy.EscapeSequence(10.10)

        with self.assertRaises(TypeError):
            pixy.EscapeSequence(10, "hello")
