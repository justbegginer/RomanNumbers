class RomanNumber:
    number: int
    _roman_number: str

    def __init__(self, number):
        self.number = number
        self.__convert_number()  # don't use description on function call , use it on the function

    def __convert_number(self):  # convert number into roman number
        roman = ""
        number = self.number
        while number >= 1000:
            number -= 1000
            roman += "M"
        while number >= 500:
            number -= 500
            roman += "D"
        while number >= 100:
            number -= 100
            roman += "C"
        while number >= 50:
            number -= 50
            roman += "L"
        while number >= 10:
            number -= 10
            roman += "X"
        while number >= 5:
            number -= 5
            roman += "V"
        while number >= 1:
            number -= 1
            roman += "I"
        if roman == "":
            self._roman_number = "0"
        else:
            self._roman_number = roman

    def __add__(self, other):
        if type(other) is str:
            return self._roman_number + other
        new_roman = RomanNumber(self.number)
        new_roman.number += other.number
        new_roman.__convert_number()
        return new_roman

    def __sub__(self, other):
        new_roman = RomanNumber(self.number)
        new_roman.number -= other.number
        new_roman.__convert_number()
        return new_roman

    def __mul__(self, other):
        new_roman = RomanNumber(self.number)
        new_roman.number *= other.number
        new_roman.__convert_number()
        return new_roman

    def __truediv__(self, other):
        new_roman = RomanNumber(self.number)
        new_roman.number //= other.number
        new_roman.__convert_number()
        return new_roman

    def __floordiv__(self, other):
        new_roman = self.__truediv__(other)
        return new_roman

    def __mod__(self, other):
        new_roman = RomanNumber(self.number)
        new_roman.number %= other.number
        new_roman.__convert_number()
        return new_roman

    def __eq__(self, other):
        if type(other) == str:
            return self._roman_number == other
        else:
            return self.number == other.number

    def __repr__(self):
        return str(self._roman_number)


first_number = RomanNumber(2)
second_number = RomanNumber(4)

assert str(first_number + second_number) == "VI", "should be six we've got "  # wtf
assert str(second_number - first_number) == "II", "should be two"
assert str(second_number / first_number) == "II" and str(
    second_number // first_number) == "II", "in both case we should get two"
assert str(second_number * first_number) == "VIII", "should be eight"
assert second_number != first_number, "numbers not equal"
