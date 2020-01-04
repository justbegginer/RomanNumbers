import unittest
from RomanNumber import RomanNumber as roman

first_number = roman(2)
second_number = roman(4)


class MyTestCase(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(first_number + second_number, "VI", "sum error")

    def test_multiply(self):
        self.assertEqual(first_number * second_number, "VIII")

    def test_div(self):
        self.assertEqual(second_number // first_number, second_number / first_number)
        self.assertEqual(second_number // first_number, "II")

    def test_div_special(self):
        first_extra = roman(3)
        second_extra = roman(2)
        self.assertEqual(first_extra // second_extra, first_extra / second_extra,
                         (first_extra// second_extra).get_number())
        self.assertEqual(first_extra // second_extra, "I")

    def test_sub(self):
        self.assertEqual(second_number - first_number, "II")

    def test_mod(self):
        self.assertEqual(second_number % first_number, "0")
        self.assertEqual(first_number % second_number, "II")


if __name__ == '__main__':
    unittest.main()
