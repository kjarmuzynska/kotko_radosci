def pole(a):
    return a**2


def division(x, y):
    if y == 0:
        raise ValueError
    return x / y

class Sim:
    def __init__(self, wlosy):
        self.wlosy = wlosy

    def przefarbuj(self, kolor):
        self.wlosy = kolor