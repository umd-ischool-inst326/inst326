import unittest
from unittest.mock import patch
from gradescope_utils.autograder_utils.decorators import weight, number
import car
from io import StringIO
from math import cos, sin, radians
import re
import sys


class CaptureCar:
    def __init__(self, x=0, y=0, heading=0):
        self.log = []
        self.x = x
        self.y = y
        self.heading = heading
        
    def turn(self, degrees):
        self.heading = (self.heading + degrees) % 360
        self.log.append(("turn", degrees))
    
    def drive(self, distance):
        self.x += sin(radians(self.heading)) * distance
        self.y -= cos(radians(self.heading)) * distance
        self.log.append(("drive", distance))


class TestCarClass(unittest.TestCase):
    def setUp(self):
        self.car1 = car.Car(x=3, y=5, heading=30)
        self.car2 = car.Car()
    
    @weight(0.5)
    @number("1.1")
    def test_init1(self):
        """ Does __init__() method work with explicit arguments? """
        self.assertEqual(self.car1.x, 3)
        self.assertEqual(self.car1.y, 5)
        self.assertEqual(self.car1.heading, 30)
    
    @weight(0.5)
    @number("1.2")
    def test_init2(self):
        """ Does __init__() method work with default argument values? """
        self.assertEqual(self.car2.x, 0)
        self.assertEqual(self.car2.y, 0)
        self.assertEqual(self.car2.heading, 0)
    
    @weight(0.5)
    @number("2.1")
    def test_turn1(self):
        """ Does turn() method work with a happy path value? """
        self.car2.turn(50)
        self.assertEqual(self.car2.heading, 50)
    
    @weight(0.5)
    @number("2.2")
    def test_turn2(self):
        """ Does turn() method work if the value is greater than 360? """
        self.car2.turn(400)
        self.assertEqual(self.car2.heading, 40)
    
    @weight(0.5)
    @number("2.3")
    def test_turn3(self):
        """ Does turn() method work if the value is negative? """
        self.car2.turn(-90)
        self.assertEqual(self.car2.heading, 270)
    
    @weight(0.5)
    @number("3.1")
    def test_drive1(self):
        """ Does drive() method work with a happy path value? """
        self.car2.drive(10)
        self.assertAlmostEqual(self.car2.x, 0)
        self.assertAlmostEqual(self.car2.y, -10)
    
    @weight(0.5)
    @number("3.2")
    def test_drive2(self):
        """ Does drive() method work with a non-zero heading? """
        self.car2.heading = 30
        self.car2.drive(10)
        self.assertAlmostEqual(self.car2.x, 5)
        self.assertAlmostEqual(self.car2.y, -8.660254037844387)
    

class TestSanityCheck(unittest.TestCase):
    def setUp(self):
        self.real_car = car.Car
        car.Car = CaptureCar
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.c = car.sanity_check()
            self.out = fake_out.getvalue()
    
    def tearDown(self):
        car.Car = self.real_car
    
    @weight(0.25)
    @number("4.1")
    def test_sanity_check1(self):
        """ Does sanity_check() return the instance it created? """
        self.assertIsInstance(self.c, CaptureCar)
    
    @weight(0.25)
    @number("4.2")
    def test_sanity_check2(self):
        """ Were the expected methods called in sanity_check()? """
        self.assertIn("turn", [i[0] for i in self.c.log])
        self.assertIn("drive", [i[0] for i in self.c.log])
        
    @weight(0.75)
    @number("4.3")
    def test_sanity_check3(self):
        """ Did sanity_check() print the expected values? """
        expr1 = r"(\d+(?:\.\d+)?),\s*(\d+(?:\.\d+)?)"
        expr2 = r"(\d+(?:\.\d+)?)"
        outlns = re.sub(r"\n{2,}", "\n", self.out.strip()).splitlines()
        self.assertEqual(len(outlns), 2)
        match1 = re.search(expr1, outlns[0])
        match2 = re.search(expr2, outlns[1])
        self.assertAlmostEqual(float(match1.group(1)), 27.320508075688775)
        self.assertAlmostEqual(float(match1.group(2)), 10)
        self.assertAlmostEqual(float(match2.group(1)), 120)


class TestDocstrings(unittest.TestCase):
    @weight(0.25)
    @number("5.1")
    def test_car_class_docstring_exists(self):
        """ Does Car class have a docstring? """
        self.assertTrue(hasattr(car.Car, "__doc__") and car.Car.__doc__)
    
    @weight(0.25)
    @number("5.2")
    def test_turn_docstring_exists(self):
        """ Does turn method have a docstring? """
        self.assertTrue(hasattr(car.Car.turn, "__doc__") and car.Car.turn.__doc__)
    
    @weight(0.25)
    @number("5.3")
    def test_drive_docstring_exists(self):
        """ Does drive method have a docstring? """
        self.assertTrue(hasattr(car.Car.drive, "__doc__") and car.Car.drive.__doc__)
