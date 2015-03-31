# -*- coding: utf8 -*-
__author__ = 'sbourdin'


class Singleton(object) :

    instance = None

    def __new__(cls):
        if Singleton.instance is None :
            Singleton.instance = object.__new__(self)
        return Singleton.instance


# On instancie un premier objet
s1 = Singleton()

# On instancie un second objet
s2 = Singleton()

# On vérifie que les deux objets sont bien identiques
assert s1 is s2

