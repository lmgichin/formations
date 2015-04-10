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
        None
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

# #############################################################################

class Carre(Rectangle):

    """
    classe représentant un carré : un rectangle spécifique où largeur = longueur
    """
    def __init__(self, x, y, cote):

        Rectangle.__init__(self, x,y,cote,cote)

    def __str__(self):
        return "CARRE"


# ##############################################################################
# code de test
# ##############################################################################

p = Point(0,0)
print p.aire()

r = Rectangle(0,0,20,10)
print r.aire()

c = Carre(0,0,10)
print c.aire()

l = [p,r,c]

for obj in l:
    print 'Aire ({}) = {}'.format( obj, obj.aire())


import doctest
doctest.testmod()










