__author__ = 'Luc Maignan'


class Point:

    cpt = 0

    def __init__(self, x, y):

        self.x, self.y = x, y
        Point.cpt += 1

    def __str__(self):
        return "Classe point : ({},{})".format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    @property
    def x(self):
        return self.x

    @x.setter
    def x(self, x):
        self.x = x

    @staticmethod
    def get_cptr():
        return Point.cpt


# ########################################################################################################

if __name__ == '__main__':

    pt = Point(2, 3)
    print pt
    pt.x = 5
    print pt + Point(4, 7)
    print Point.get_cptr()
    print help(Point)