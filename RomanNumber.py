class RomanNumber:
    _number: int
    _roman_number: str

    def __init__(self, number):
        if type(number) is int or \
                type(number) is RomanNumber:
            self.set_number(number)  # don't use description on function call , use it on the function
        elif type(number) is str:
            self.convert_string_roman_to_number(string=number)
        else:
            raise TypeError

    @property
    def get_number(self):
        return self._number

    def set_number(self, new_number):
        if type(new_number) is RomanNumber:
            self._number = new_number.get_number
        else:
            self._number = new_number
        self.__convert_number()  # every time we set number ,  we reconvert the roman number

    def __convert_number(self):  # convert number into roman number
        roman = ""
        number = self.get_number
        if number < 0:
            number = abs(number)
            roman = "-"
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
        if roman == "":  # if string is empty that means that number was equal zero
            self._roman_number = "0"
        else:
            self._roman_number = roman

    def convert_string_roman_to_number(self, string):
        result = 0
        convert_to_negative = False
        if string[0] == "-":
            string = string[1:]
            convert_to_negative = True
        for i in string:
            if i == "M":
                result += 1000
            elif i == "D":
                result += 500
            elif i == "C":
                result += 100
            elif i == "L":
                result += 50
            elif i == "X":
                result += 10
            elif i == "V":
                result += 5
            elif i == "I":
                result += 1
            elif i == "0":
                pass
            else:
                raise ValueError
        if convert_to_negative:
            result = -result
        self.set_number(result)

    @staticmethod
    def __different_types_operations(other):
        if type(other) is int or \
                type(other) is str:
            new_roman = RomanNumber(other)
            return new_roman
        else:
            return other

    def __str__(self):
        return self._roman_number

    def __int__(self):
        return self.get_number

    def __math_operation(self, other, func):
        other = RomanNumber.__different_types_operations(other)
        return RomanNumber(func(self.get_number, other.get_number))

    def __add__(self, other):
        return self.__math_operation(other, lambda x, y: x + y)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self.__math_operation(other, lambda x, y: x - y)

    def __rsub__(self, other):
        return self.__math_operation(other, lambda x, y: y - x)  # reversed lambda function

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        return self.__math_operation(other, lambda x, y: x * y)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return self.__math_operation(other, lambda x, y: x // y)

    def __rtruediv__(self, other):
        return self.__math_operation(other, lambda x, y: y // x)

    def __itruediv__(self, other):
        return self.__truediv__(other)

    def __floordiv__(self, other):
        return self.__truediv__(other)

    def __rfloordiv__(self, other):
        return self.__rtruediv__(other)

    def __ifloordiv__(self, other):
        return self.__floordiv__(other)

    def __mod__(self, other):
        return self.__math_operation(other, lambda x, y: x % y)

    def __rmod__(self, other):
        return self.__math_operation(other, lambda x, y: y % x)

    def __imod__(self, other):
        return self.__mod__(other)

    def __pow__(self, power, modulo=None):
        return self.__math_operation(power, lambda x, y: x ** y)

    def __rpow__(self, power):
        return self.__math_operation(power, lambda x, y: y ** x)

    def __ipow__(self, power):
        return self.__pow__(power)

    def __or__(self, other):
        return self.__math_operation(other, lambda x, y: x | y)

    def __ror__(self, other):
        return self.__or__(other)

    def __ior__(self, other):
        return self.__or__(other)

    def __and__(self, other):
        return self.__math_operation(other, lambda x, y: x & y)

    def __rand__(self, other):
        return self.__and__(other)

    def __iand__(self, other):
        return self.__and__(other)

    def __xor__(self, other):
        return self.__math_operation(other, lambda x, y: x ^ y)

    def __rxor__(self, other):
        return self.__xor__(other)

    def __ixor__(self, other):
        return self.__xor__(other)

    def __lt__(self, other):
        other = RomanNumber.__different_types_operations(other)
        return self.get_number < other.get_number

    def __gt__(self, other):
        other = RomanNumber.__different_types_operations(other)
        return self.get_number > other.get_number

    def __le__(self, other):
        return self.__lt__(other) or self == other

    def __ge__(self, other):
        return self.__gt__(other) or self == other

    def __bool__(self):
        return self.get_number

    def __eq__(self, other):
        other = RomanNumber.__different_types_operations(other)
        return self.get_number == other.get_number

    def __repr__(self):
        return str(self._roman_number)
