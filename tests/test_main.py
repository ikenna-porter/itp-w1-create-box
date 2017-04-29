import unittest

from create_box import create_box
from create_box import create_box_empty


first_box_expected = """
****
****
****
""".lstrip()

second_box_expected = """
@
""".lstrip()

third_box_expected = """
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
""".lstrip()


class TestCreateBox(unittest.TestCase):
    def test_box(self):
        self.assertEqual(create_box(3, 4, '*'), first_box_expected)

    def test_small_box(self):
        self.assertEqual(create_box(1, 1, '@'), second_box_expected)
        
    def test_small_box_full(self):
        self.assertEqual(create_box(1, 0, '@'), "Invalid Entry")

    # Add your own test using third_box_expected
    
    

first_box_expected1 = """
****
*  *
****
""".lstrip()

second_box_expected1 = """
@
""".lstrip()

third_box_expected1 = """
XXXXXXXXX
X       X
X       X
XXXXXXXXX
""".lstrip()


class TestCreateBox_empty(unittest.TestCase):
    def test_box(self):
        self.assertEqual(create_box_empty(3, 4, '*'), first_box_expected1)

    def test_small_box1(self):
        self.assertEqual(create_box_empty(1, 1, '@'), second_box_expected1)
        
    def test_small_box2(self):
        self.assertEqual(create_box_empty(1, 0, '@'), "Invalid Entry")
    
    def test_small_box3(self):
        self.assertEqual(create_box_empty(4, 9, 'X'), third_box_expected1)
             
 
