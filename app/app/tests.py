
from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """ 
    Test calc module

    """

    def test_add_numbers(self):
        """ 
        Test adding numbers together

        """
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_sub_numbers(self):
        res = calc.subtract(7, 2)
        self.assertEqual(res, 5)
