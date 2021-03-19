import unittest
from hexnumber.hex_num import *

class TextNexNumber(unittest.TestCase):

    def test_check_num(self):
        num = 'A203B'
        expect = True
        result = check_num(num)
        self.assertEqual(expect, result)
        num = 'A2c3B'
        expect = False
        result = check_num(num)
        self.assertEqual(expect, result)

    def test_check_char(self):
        char = 'A'
        expect = True
        result = check_char(char)
        self.assertEqual(expect, result)
        char = '4'
        expect = True
        result = check_char(char)
        self.assertEqual(expect, result)
        char = 'c'
        expect = False
        result = check_char(char)
        self.assertEqual(expect, result)

    def test_char_to_num(self):
        char = 'A'
        expect = 10
        result = char_to_num(char)
        self.assertEqual(expect, result)
        char = '9'
        expect = 9
        result = char_to_num(char)
        self.assertEqual(expect, result)

    def test_num_to_char(self):
        num = 12
        expect = 'C'
        result = num_to_char(num)
        self.assertEqual(expect, result)
        num = 3
        expect = '3'
        result = num_to_char(num)
        self.assertEqual(expect, result)

    def test_to_str(self):
        num = HexNumber('ABCDEF12345')
        expect = 'ABCDEF12345'
        result = str(num)
        self.assertEqual(expect, result)

    def test_add(self):
        num1 = HexNumber('ABCDEF')
        num2 = HexNumber('1')
        expect = 'ABCDF0'
        result = str((num1 + num2))
        self.assertEqual(expect, result)
        num1 = HexNumber('F1BC4F')
        num2 = HexNumber('FFFFF')
        expect = '101BC4E'
        result = str((num1 + num2))
        self.assertEqual(expect, result)

if __name__ == '__main__':
    unittest.main()
