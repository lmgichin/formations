# -*- coding: utf-8 -*-

# #######################################################################################
# sample démontrant le polymorphisme en Python
# #######################################################################################

class Point:

    """
    classe représentant un point
    """
    def __init__(self,x,y):

        self.x, self.y= x,y


    def aire(self):
        """
        >>> p = Point(0,0)
        >>> print p.aire()
        x
        """
        return None

    def __str__(self):
        return "POINT"

# #######################################################################################

class Rectangle(Point):

    """
    classe représentant un rectangle : un point (origine), une largeur et une longueur
    """
    def __init__(self, x, y, lg, la):

        Point.__init__(self, x, y)
        self.lg, self.la = lg, la

    def aire(self):

        return self.lg * self.la

    def __str__(self):

        return "RECTANGLE"

    def __gt__(self, other):

        return self.aire() > other.aire()

    def __lt__(self, other):

        return self.aire() < other.aire()



# #############################################################################


class Carre(Rectangle):

    """
    classe représentant un carré : un rectangle spécifique où largeur = longueur
    """
    def __init__(self, x, y, cote):

        Rectangle.__init__(self, x, y, cote, cote)
        self.cote = cote

    def __str__(self):
        return "CARRE"

    def __add__(self, other):
        return Carre(self.x, self.y, self.cote + other.cote)

    def ta(self):
        """
        >>> c = Carre(4)
        >>> print c.aire()
        16
        """
        return None


# ##############################################################################
# code de test
# ##############################################################################

p = Point(0,0)
print p.aire()

r = Rectangle(0,0,20,10)
print r.aire()

r2 = Rectangle(0,0,25,10)
print r2.aire()

c = Carre(0,0,2)
print c.aire()

c2 = Carre(0,0,5)
print c2.aire()

print c2 > c

print c2.__class__



l = [p,r,c]

for obj in l:
    print 'Aire ({}) = {}'.format( obj, obj.aire())













