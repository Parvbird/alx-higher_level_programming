"""this function defines test cases for Base class"""


import unittest
import os
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    """ the test cases for Base class """

    def test_id_passed(self):
        """ the test for id passed as argument """
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_id_not_passed(self):
        """ the test for no argument """
        b2 = Base()
        self.assertEqual(b2.id, 5)

    def test_private_class_instance(self):
        """ the test to access private class instance """
        b3 = Base()
        with self.assertRaises(AttributeError):
            print(b3.__nd_objects)

    def test_to_json_rep_method(self):
        """ the test for json representation """
        r1 = Rectangle(10, 7, 2, 8)
        # this is to convert to regular object dictionary
        dictionary = r1.to_dictionary()
        self.assertEqual(str(type(dictionary)), "<class 'dict'>")
        # this to convert to json represention
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(str(type(json_dictionary)), "<class 'str'>")
        # this is when parameter is empty or None
        empty_dictionary = Base.to_json_string(None)
        self.assertEqual(str(empty_dictionary), "[]")

    def test_save_to_file(self):
        """ the test to save to a json or .csv file """
        # the first for Rectangle class
        r2 = Rectangle(13, 3, 1, 0)
        r3 = Rectangle(10, 8)
        # this saves to .json file
        Rectangle.save_to_file([r2, r3])
        with open("Rectangle.json", "r", encoding="UTF-8") as r_file:
            r_file.read()
        self.assertTrue(os.path.exists("Rectangle.json"))
        # save to .csv file
        Rectangle.save_to_file_csv([r2, r3])
        with open("Rectangle.csv", "r", encoding="UTF-8") as csv_file:
            csv_file.read()
        self.assertTrue(os.path.exists("Rectangle.csv"))

        # the next for Square class
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        # this saves to .json file
        Square.save_to_file([s1, s2])
        with open("Square.json", "r", encoding="UTF-8") as s_file:
            s_file.read()
        self.assertTrue(os.path.exists("Square.json"))
        # this saves to .csv file
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r", encoding="UTF-8") as s_file:
            s_file.read()
        self.assertTrue(os.path.exists("Square.csv"))

    def test_save_to_file_empty_list_for_Square(self):
        """ the test to save an empty list for Square object """
        # this saves to .json file
        Square.save_to_file(None)
        with open("Square.json", "r", encoding="UTF-8") as s_file:
            s_file.read()
        self.assertTrue(os.path.exists("Square.json"))
        # this saves to .csv file
        Square.save_to_file_csv(None)
        with open("Square.csv", "r", encoding="UTF-8") as s_file:
            s_file.read()
        self.assertTrue(os.path.exists("Square.csv"))

    def test_save_to_file_argument_None_for_Square(self):
        """ the test to save when argument is None for Square object"""
        # this saves to .json file
        Square.save_to_file([])
        with open("Square.json", "r", encoding="UTF-8") as s_file:
            s_file.read()
        self.assertTrue(os.path.exists("Square.json"))
        # this saves to .csv file
        Square.save_to_file_csv([])
        with open("Square.csv", "r", encoding="UTF-8") as s_file:
            s_file.read()
        self.assertTrue(os.path.exists("Square.csv"))

    def test_save_to_file_empty_list_for_Rectangle(self):
        """ the test for save an empty list for Rectangle object """
        # this saves to .json file
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r", encoding="UTF-8") as s_file:
            s_file.read()
        self.assertTrue(os.path.exists("Rectangle.json"))
        # this saves to .csv file
        Rectangle.save_to_file(None)
        with open("Rectangle.csv", "r", encoding="UTF-8") as s_file:
            s_file.read()
        self.assertTrue(os.path.exists("Rectangle.csv"))

    def test_save_to_file_argument_None_for_Rectangle(self):
        """ the test to save when argument is None for Rectangle object """
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r", encoding="UTF-8") as s_file:
            s_file.read()
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_from_json_string_non_empty_list(self):
        """ the test for deserialization of non-empty list """
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)

    def test_from_json_string_empty_list(self):
        """ the test for deserialization of empty list """
        list_input = []
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)

    def test_from_json_string_None_argument(self):
        """ the test for deserialization when argument is None """
        json_list_input = Rectangle.to_json_string(None)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)

    def test_create_Rectangle_class(self):
        """ the test for create method """
        r4 = Rectangle(3, 5, 1)
        r4_dictionary = r4.to_dictionary()
        r5 = Rectangle.create(**r4_dictionary)
        self.assertEqual(str(r4), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(str(r5), "[Rectangle] (1) 1/0 - 3/5")
        self.assertFalse(r4 is r5)
        self.assertFalse(r4 == r5)

    def test_create_Square_class(self):
        """ the test for create method """
        s4 = Square(3, 5, 1)
        s4_dictionary = s4.to_dictionary()
        s5 = Square.create(**s4_dictionary)
        self.assertEqual(str(s4), "[Square] (3) 5/1 - 3")
        self.assertEqual(str(s5), "[Square] (3) 5/1 - 3")
        self.assertFalse(s4 is s5)
        self.assertFalse(s4 == s5)

    def test_load_from_file_Rectangle_class(self):
        """
        the test to load data from a Rectangle.json file
        & returns the list of instances
        """
        r6 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [r6]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertFalse(list_rectangles_input is list_rectangles_output)
        self.assertFalse(list_rectangles_input == list_rectangles_output)

    def test_load_from_file_Square_class(self):
        """
        the test to load data from a Square.json file
        & return the list of instances
        """
        r6 = Square(7, 9, 1)
        list_squares_input = [r6]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertFalse(list_squares_input is list_squares_output)
        self.assertFalse(list_squares_input == list_squares_output)
