import unittest
from RomanNumber import RomanNumber as roman
from unittest import TestCase as tCase

first_number = roman(2)
second_number = roman(4)


class SimpleMathTest(tCase):
    def test_sum(self):
        self.assertEqual(first_number + second_number, "VI", "sum error")

    def test_sub(self):
        self.assertEqual(second_number - first_number, "II")

    def test_multiply(self):
        self.assertEqual(first_number * second_number, "VIII")

    def test_div(self):
        self.assertEqual(second_number // first_number, second_number / first_number)
        self.assertEqual(second_number // first_number, "II")
        self.assertEqual(4 / first_number, 2)

    def test_div_special(self):
        first_extra = roman(3)
        second_extra = roman(2)
        self.assertEqual(first_extra // second_extra, first_extra / second_extra,
                         (first_extra // second_extra).get_number)
        self.assertEqual(first_extra // second_extra, "I")

    def test_mod(self):
        self.assertEqual(second_number % first_number, "0")
        self.assertEqual(first_number % second_number, "II")

    def test_pow(self):
        self.assertEqual(first_number ** second_number, 16)

    def test_minus(self):
        self.assertEqual(first_number - second_number, "-II")
        self.assertEqual((first_number - second_number) * first_number, "-IIII")


class rMathTest(tCase):
    def test_radd(self):
        self.assertEqual(3 + first_number, roman(5))

    def test_rsub(self):
        self.assertEqual(6 - second_number, 2)

    def test_rmultiply(self):
        self.assertEqual(7 * first_number, roman(14))

    def test_rdiv(self):
        self.assertEqual(16 / second_number, 4)
        self.assertEqual(15 // first_number, 7)

    def test_rmod(self):
        self.assertEqual(4 % first_number, 0)

    def test_rpow(self):
        self.assertEqual(3 ** second_number, 81)


class IMathTest(tCase):

    def test_iadd(self):
        new_roman = roman(3)
        new_roman += 3
        self.assertEqual(new_roman, 6)

    def test_isub(self):
        new_roman = roman(3)
        new_roman -= 3
        self.assertEqual(new_roman, 0)

    def test_imul(self):
        new_roman = roman(3)
        new_roman *= 3
        self.assertEqual(new_roman, 9)

    def test_itruediv(self):
        new_roman = roman(3)
        new_roman //= 3
        self.assertEqual(new_roman, 1)

    def test_ifloordiv(self):
        new_roman = roman(3)
        new_roman /= 3
        self.assertEqual(new_roman, 1)

    def test_imod(self):
        new_roman = roman(3)
        new_roman %= 3
        self.assertEqual(new_roman, 0)

    def test_pow(self):
        new_roman = roman(3)
        new_roman **= 3
        self.assertEqual(new_roman, 27)


class ComparisonTest(tCase):
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


class BooleanAlgebra(tCase):
    def test_or(self):
       self.assertEqual(roman(8) | roman(3), 11)

    def test_and(self):
        self.assertEqual(roman(2) & roman(3), 2)

    def test_xor(self):
        self.assertEqual(roman(7) ^ roman(4), 3)

    def test_ior(self):
        new_roman = roman(8)
        new_roman |= roman(3)
        self.assertEqual(new_roman, 11)

    def test_iand(self):
        new_roman = roman(2)
        new_roman &= roman(3)
        self.assertEqual(new_roman, 2)

    def test_ixor(self):
        new_roman = roman(7)
        new_roman ^= roman(4)
        self.assertEqual(new_roman, 3)


class SpecialFunctionsTest(tCase):

    def test_init(self):
        with self.assertRaises(ValueError) as v_exc:
            roman("Mn")
        with self.assertRaises(Exception) as exc:
            roman()
        self.assertEqual(roman(10), "X")
        self.assertEqual(roman("XV"), 15)

    def test__different_types_of_operations_func(self):
        self.assertEqual(first_number + 3, 5)
        self.assertEqual(second_number - 2, first_number)
        self.assertEqual(first_number * 2, second_number)
        self.assertEqual(second_number / 2, first_number)
        self.assertEqual(second_number // 2, first_number)
        self.assertEqual(first_number % 4, 2)

    def test_str(self):
        self.assertEqual(str(second_number) + str(first_number), "IIIIII")


if __name__ == '__main__':
    unittest.main()
