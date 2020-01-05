class RomanNumber:
    _number: int
    _roman_number: str

    def __init__(self, number=None, string=None):
        if number is not None:
            self.set_number(number)  # don't use description on function call , use it on the function
            if type(number) is not int:
                raise TypeError
        elif string is not None:
            self.convert_string_roman_to_number(string=string)
            if type(string) is not str:
                raise TypeError
        else:
            assert False, "Argument exception"

    def get_number(self):
        return self._number

    def set_number(self, new_number):
        self._number = new_number
        self.__convert_number()  # every time we set number ,  we reconvert the roman number

    def __convert_number(self):  # convert number into roman number
        roman = ""
        number = self.get_number()
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
        if roman == "":
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
            else:
                raise ValueError
        if convert_to_negative:
            result = -result
        self.set_number(result)

    def __add__(self, other):
        if type(other) is str:
            return self._roman_number + other
        new_roman = RomanNumber(self.get_number())
        new_roman.set_number(self.get_number() + other.get_number())
        return new_roman

    def __sub__(self, other):
        new_roman = RomanNumber(self.get_number())
        new_roman.set_number(self.get_number() - other.get_number())
        return new_roman

    def __mul__(self, other):
        new_roman = RomanNumber(self.get_number())
        new_roman.set_number(self.get_number() * other.get_number())
        return new_roman

    def __truediv__(self, other):
        new_roman = RomanNumber(self.get_number())
        new_roman.set_number(self.get_number() // other.get_number())
        return new_roman

    def __floordiv__(self, other):
        new_roman = self.__truediv__(other)
        return new_roman

    def __mod__(self, other):
        new_roman = RomanNumber(self.get_number())
        new_roman.set_number(self.get_number() % other.get_number())
        return new_roman

    def __eq__(self, other):
        if type(other) is str:
            return self._roman_number == other
        elif type(other) is int:
            return self.get_number() == other
        else:
            return self.get_number() == other.get_number()

    def __repr__(self):
        return str(self._roman_number)
