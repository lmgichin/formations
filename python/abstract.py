# -*- coding: utf-8 -*-

__author__ = 'Luc Maignan'


# #######################################################################################################
# ancienne méthode < 2.6
# #######################################################################################################

class AbstractOld(object):

    def __init__(self):
        pass

    def abstract_method(self):
        raise NotImplementedError


# ######################################################################################################
# nouvelle méthode >= 2.6
# ######################################################################################################

import abc

get_gen = lambda cls,attr: cls.__dict__[attr]

class AbstractNew(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        print "AN -> init"
        self.val = 'hello'

    @abc.abstractmethod
    def method1(self):
        print "AN -> method1"


class Abs2(AbstractNew):

    def method1(self,x):

        AbstractNew.method1(self)
        print "ABS2 -> method1"
        print get_gen(self,'val')


# ######################################################################################################
# création dynamique d'une classe
# ######################################################################################################

def cl_create(inst, nom, prenom):

    inst.nom = nom
    inst.prenom = prenom


def cl_print(inst):

    print "Nom = {}, prénom = {}".format(inst.nom, inst.prenom)


# ######################################################################################################
# Test
# ######################################################################################################

if __name__ == '__main__':

    ao = AbstractOld()
    print "Instance valide = ", ao is not None

    try:
        ao2 = AbstractNew()
    except TypeError:
        print "Erreur : impossible d'instancier une classe abstraite"
    finally:
        ao2 = Abs2()
        ao2.method1(3)
        help(ao2)
        print "On peut sous-classer la classe abstraite...\n\tsi on implémente la méthode abstraite"

    print "*** Création dynamique de la classe Personne"
    methodes = {"__init__": cl_create, "affiche": cl_print}
    Personne = type("Personne", (), methodes)
    pers = Personne("Funakoshi", "Gichin")
    pers.affiche()