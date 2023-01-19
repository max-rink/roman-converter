import unittest

from app import main


class TestMain(unittest.TestCase):
    def test_roman_single_digit(self, expected_result, test_result):
        self.assertEqual(expected_result, test_result)

    def test_roman_multiple_digit(self, expected_result, test_result):
        self.assertEqual(expected_result, test_result)

    def test_convert_roman_to_int(self):
        # 0
        data = ''
        result = main.convert_roman_to_int(data)
        self.assertEqual(0, 'result')



        TestMain.test_roman_single_digit(1, 'I')
        TestMain.test_roman_single_digit(5, 'V')
        TestMain.test_roman_single_digit(10, 'X')
        TestMain.test_roman_single_digit(50, 'L')
        TestMain.test_roman_single_digit(100, 'C')
        TestMain.test_roman_single_digit(500, 'D')
        TestMain.test_roman_single_digit(1000, 'M')

        data = 'VI'
        result = main.convert_roman_to_int(data)
        self.assertEqual(6, result)


if __name__ == '__main__':
    unittest.main()
