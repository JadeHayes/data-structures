def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + \
                 self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den

        return first_num == second_num

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den

        return f"{new_num}/{new_den}"

    def __sub__(self, other):
        new_num = self.num * other.den - \
                  self.den * other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)

        return Fraction(new_num//common, new_den//common)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num

        common = gcd(new_num, new_den)

        return Fraction(new_num//common, new_den//common)

    def __lt__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.den

        return first_num < second_num

    def __gt__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.den

        return first_num > second_num


x = Fraction(4, 5)
y = Fraction(1, 10)
print(x+y)
print(x == y)
print(x - y)
print(x / y)