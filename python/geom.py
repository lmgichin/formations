class Point:

    def __init__(self,x,y):

        self.x, self.y= x,y


    def aire(self):

        return None

    def __str__(self):
        return "POINT"

class Rectangle(Point):

    def __init__(self, x, y, lg, la):

        Point.__init__(self, x, y)
        self.lg, self.la = lg, la

    def aire(self):

        return self.lg * self.la

    def __str__(self):
        return "RECTANGLE"


class Carre(Rectangle):

    def __init__(self, x, y, cote):

        Rectangle.__init__(self, x,y,cote,cote)

    def __str__(self):
        return "CARRE"



p = Point(0,0)
print p.aire()

r = Rectangle(0,0,20,10)
print r.aire()

c = Carre(0,0,10)
print c.aire()

l = [p,r,c]

for obj in l:
    print 'Aire ({}) = {}'.format( obj, obj.aire())













