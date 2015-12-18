# -*- coding: UTF-8 -*-
__author__ = 'lmaignan'

class Somme:

    def __init__(self, p1, p2):

        self.p1, self.p2 = p1, p2

    @property
    def p1(self):
        return self.p1

    @p1.setter
    def p1(self,val):
        self.p1 = val

    def sum(self):

        return self.p1 + self.p2

    @staticmethod
    def what():
        return "MA CLASSE SOMME"

    def __str__(self):
        return "Classe somme param 1 = {}, param 2= {}".format(self.p1, self.p2)

    def __repr__(self):
        return "Classe (REPR) somme param 1 = {}, param 2= {}".format(self.p1, self.p2)


"""class Somme3(Somme):

        def __init__(self, p1, p2, p3):
        #Somme.__init__(self,p1,p2)
        super(Somme3,self).__init__(p1,p2)
        self.p3 = p3

    def sum(self):

        #return self.p1 + self.p2 + self.p3
        return Somme.sum(self)  + self.p3
"""
if __name__ == '__main__':

    ms = Somme(2,3)

    ms.p1 = 7
    #print "Value of p1 = ", ms.p1
    print ms.sum()
    print Somme.what()
    print repr(ms)
"""
    ms3 = Somme3(1,2,3)
    print ms3.sum()


    #help(ms)

"""




