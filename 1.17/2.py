#  Modify the constructor for the Fraction class so that GCD is used to reduce fractions immediately.

def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
        # use gcd to auto reduce
        common = gcd(top,bottom)
        self.num = self.num//common
        self.den = self.den//common

    def __str__(self):
        return "{:d}/{:d}".format(self.num, self.den)

    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den

        return first_num == second_num

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den \
        + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction

    def show(self):
        print("{:d}/{:d}".format(self.num, self.den))

my_fraction = Fraction(32, 64)
# expect 1/2
my_fraction.show()

my_fraction = Fraction(6, 8)
# expect 3/4
my_fraction.show()
