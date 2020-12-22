#
# Copyright (c) 2020 Kian Cross
#

import unittest
import pixy


class DecoratorTests(unittest.TestCase):
    def test_bold(self):
        self.assertEqual(pixy.decorators.bold.code, "\x1b[1m")

    def test_faint(self):
        self.assertEqual(pixy.decorators.faint.code, "\x1b[2m")

    def test_italic(self):
        self.assertEqual(pixy.decorators.italic.code, "\x1b[3m")

    def test_underline(self):
        self.assertEqual(pixy.decorators.underline.code, "\x1b[4m")

    def test_slow_blink(self):
        self.assertEqual(pixy.decorators.slow_blink.code, "\x1b[5m")

    def test_rapid_blink(self):
        self.assertEqual(pixy.decorators.rapid_blink.code, "\x1b[6m")

    def test_invert(self):
        self.assertEqual(pixy.decorators.invert.code, "\x1b[7m")

    def test_conceal(self):
        self.assertEqual(pixy.decorators.conceal.code, "\x1b[8m")

    def test_strike(self):
        self.assertEqual(pixy.decorators.strike.code, "\x1b[9m")

    def test_fraktur(self):
        self.assertEqual(pixy.decorators.fraktur.code, "\x1b[20m")

    def test_double_underline(self):
        self.assertEqual(pixy.decorators.double_underline.code, "\x1b[21m")

    def test_framed(self):
        self.assertEqual(pixy.decorators.framed.code, "\x1b[51m")

    def test_encircled(self):
        self.assertEqual(pixy.decorators.encircled.code, "\x1b[52m")

    def test_overlined(self):
        self.assertEqual(pixy.decorators.overlined.code, "\x1b[53m")
