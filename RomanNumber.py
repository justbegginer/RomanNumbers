class RomanNumber:
    number: int
    _roman_number: str

    def __init__(self, number):
        self.number = number
        self.__convert_number()  # don't use description on function call , use it on the function

    def __convert_number(self):  # convert number into roman number
        roman = ""
        number = self.number
        while number > 1000:
            number -= 1000
            roman += "M"

    def __add__(self, other):
        self.number += other.number
        self.__convert_number()
        return self

    def __sub__(self, other):
        self.number -= other.number
        self.__convert_number()
        return self

    def __mul__(self, other):
        self.number *= other.number
        self.__convert_number()
        return self

    def __truediv__(self, other):
        self.number //= other.number
        self.__convert_number()
        return self

    def __floordiv__(self, other):
        return self.__truediv__(self, other)

    def __mod__(self, other):
        self.number %= other.number
        self.__convert_number()
        return self

    def __eq__(self, other):
        return self == other

    def __repr__(self):
        return self._roman_number
