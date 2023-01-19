import unittest

from app import main


class TestMain(unittest.TestCase):
    def test_roman_single_digit(self):
        self.assertEqual(1, main.convert_roman_to_int('I'))
        self.assertEqual(5, main.convert_roman_to_int('V'))
        self.assertEqual(10, main.convert_roman_to_int('X'))
        self.assertEqual(50, main.convert_roman_to_int('L'))
        self.assertEqual(100, main.convert_roman_to_int('C'))
        self.assertEqual(500, main.convert_roman_to_int('D'))
        self.assertEqual(1000, main.convert_roman_to_int('M'))

    def test_substraction_units(self):
        self.assertEqual(4, main.convert_roman_to_int('IV'))
        self.assertEqual(9, main.convert_roman_to_int('IX'))
        self.assertEqual(40, main.convert_roman_to_int('XL'))
        self.assertEqual(90, main.convert_roman_to_int('XC'))
        self.assertEqual(400, main.convert_roman_to_int('CD'))
        self.assertEqual(900, main.convert_roman_to_int('CM'))

    def test_parsing_units(self):
        self.assertEqual(['I','I'], main.unitparser('II'))
        self.assertEqual(['XL','IX'], main.unitparser('XLIX'))
        self.assertEqual(['X','X','I'], main.unitparser('XXI'))
        self.assertNotEqual(['I','V'], main.unitparser('IV'))

    def test_convert_roman_to_int(self):
        # 0
        data = ''
        result = main.convert_roman_to_int(data)
        self.assertEqual(0, result)

        self.test_roman_single_digit()
        self.test_substraction_units()


if __name__ == '__main__':
    unittest.main()
