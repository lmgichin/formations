class Pers:

    def __init__(self,nom):
        self.nom

    def get(self):
        """
        >>> p = Pers()
        >>> print p.get()
        PERS
        """
        return "PERS"

class PP(Pers):

    nb = 0
    def __init__(self,nom):
        self.nom = nom

    def __del__(self):
        pass

    def __str__(self):
        return "Personne " + self.nom

    def __repr__(self):
        return "Personne " + self.nom

    def get_nom(self):
        return self.get() + self.nom

    @staticmethod
    def get_name():
        return "CLASS PP"

    @classmethod
    def infos(cls):
        print dir(cls)


pers1 = PP('Hugo')
print pers1.get_nom()
print str(pers1)
print PP.get_name()
print pers1.__class__.__name__
l = [pers1]
print l[0].get_nom()

for p in l:
    print p.get_nom()

pers1.infos()
print dir(PP)
