#!/usr/bin/python

import inspect
import os
import sys
import unittest

sys.path = [ os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) ] + sys.path
from init_subclass import InitSubclass


class Philosopher(InitSubclass):
    subclasses = []

    def __init_subclass__(cls):
        Philosopher.subclasses.append(cls.__name__)


class Test(unittest.TestCase):
    def test_basic(self):
        class Socrates(Philosopher):
            pass
        class Plato(Philosopher):
            pass

        self.assertEquals(
            Philosopher.subclasses,
            ['Socrates', 'Plato'],
        )


    def test_dynamic(self):
        Loki = type(
            'Loki',
            (Philosopher,),
            {}
        )

        self.assertIn(
            'Loki',
            Philosopher.subclasses,
        )



if __name__ == '__main__':
    unittest.main()
