import unittest
from RomanNumber import RomanNumber as roman

first_number = roman(2)
second_number = roman(4)


class MyTestCase(unittest.TestCase):
    def test_init(self):
        self.assertEqual(roman(10), "X")
        self.assertEqual(roman("XV"), 15)
        try:
            roman("Mn")
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
                         (first_extra // second_extra).get_number)
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
        self.assertTrue(first_number == 2)
        self.assertTrue(second_number == 4)

    def test_compare(self):
        self.assertTrue(first_number < 4)  # __lt__ override function
        self.assertTrue(3 > first_number)

    def test_not_equal(self):
        self.assertTrue(first_number != second_number)

    def test_compare_or_equal(self):
        self.assertTrue(first_number >= 2)
        self.assertTrue(first_number <= 2)


if __name__ == '__main__':
    unittest.main()
