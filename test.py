import unittest
from RomanNumber import RomanNumber as roman

first_number = roman(2)
second_number = roman(4)


class MyTestCase(unittest.TestCase):
    def test_init(self):
        self.assertEqual(roman(10), "X")
        self.assertEqual(roman(string="XV"), 15)
        try:
            roman(string="Mn")
        except ValueError:
            pass
        else:
            raise ValueError
        try:
            roman()
        except Exception:
            pass
        else:
            raise Exception

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
                         (first_extra // second_extra).get_number())
        self.assertEqual(first_extra // second_extra, "I")

    def test_sub(self):
        self.assertEqual(second_number - first_number, "II")

    def test_mod(self):
        self.assertEqual(second_number % first_number, "0")
        self.assertEqual(first_number % second_number, "II")

    def test_minus(self):
        self.assertEqual(first_number - second_number, "-II")
        self.assertEqual((first_number - second_number) * first_number, "-IIII")

    def test_equal(self):
        self.assertEqual(first_number, 2)
        self.assertEqual(second_number, 4)


if __name__ == '__main__':
    unittest.main()
