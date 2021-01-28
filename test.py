import unittest
import pandas

from dish_selector_2 import read_menu

class TestDish(unittest.TestCase):
    def test_read_menu(self):
        """
        Test that read_menu function can read database
        """
        menu_type = 'main_course'
        result = read_menu(menu_type).shape[0] > 0
        message = "0 rows read from " + menu_type
        self.assertTrue(result, message)