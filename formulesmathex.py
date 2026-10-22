from math import atan2, sqrt


class Complexe:
    def __init__(self, re=0.0, im=0.0):
        self.re = re
        self.im = im

    def __neg__(self):
        return Complexe(-self.re, -self.im)

    def __str__(self):
        if self.re == 0 and self.im == 0:
            return '0'
        elif self.re == 0:
            return f'{self.im}i'
        elif self.im == 0:
            return f'{self.re}'
        elif self.im == 1:
            return f'{self.re}+i'
        elif self.im == -1:
            return f'{self.re}-i'
        elif self.im > 0:
            return f'{self.re}+{self.im}i'
        else:
            return f'{self.re}{self.im}i'

    def conjugue(self):
        return Complexe(self.re, -self.im)

    def module(self):
        return sqrt(self.re**2 + self.im**2)

    def ajouter(self, z2):
        if isinstance(z2, (float, int)):
            z2 = Complexe(z2, 0)
        return Complexe(self.re + z2.re, self.im + z2.im)

    def soustraire(self, z2):
        return self.ajouter(-z2)

    def multiplier(self, z2):
        if isinstance(z2, (float, int)):
            z2 = Complexe(z2, 0)
        return Complexe(self.re * z2.re + self.im * z2.im * -1, self.re * z2.im + self.im * z2.re)

    def inverse(self):
        return self.conjugue().multiplier(1 / self.module()**2)

    def diviser(self, z2):
        if isinstance(z2, (float, int)):
            z2 = Complexe(z2, 0)
        return self.multiplier(z2.inverse())

    def puissance(self, n):
        if n > 0:
            return self.multiplier(self.puissance(n - 1))
        elif n < 0:
            return self.inverse().puissance(-n)
        else:
            return Complexe(1, 0)

    def argument(self):
        return atan2(self.im, self.re)

    def forme_exponentielle(self):
        return f'{self.module()} * e^(i * {self.argument()})'
