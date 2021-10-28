# Implement the simple methods get_num and get_den that will return the numerator and denominator of a fraction.

class Fraction:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

    def get_num(self):
        return self.top

    def get_den(self):
        return self.bottom

my_fraction = Fraction(3,4)
print(my_fraction.get_num())
print(my_fraction.get_den())