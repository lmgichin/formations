# -*- coding: utf8 -*-

class Personne:
    "Définition de la classe personne"

    # Pas de surcharge
    # Pas de polymorphisme direct

    ### Attributs statiques de classe ###
    ctr = 0

    ### Attributs d'instance ###
    # Pas de définition préalable

    ### Méthode appelée avant la création de l'instance ###
    def __new__(self):
        pass

    ### Constructeur ###
    def __init__(self, nom, prenom):
        Personne.ctr += 1
        self.nom = nom
        self.prenom = prenom

    ### Destructeur ###
    def __del__(self):
        pass

    ### Méthode sollicitée par str ###
    def __str__(self):
        return self.prenom + " " + self.nom

    ### Méthode statique ###
    def get_ctr():
        return Personne.ctr

    ### getter, setter ###
    @property
    def name(self):
        return self.nom

    @name.setter
    def name(self, name):
        self.nom = name

    get_ctr = staticmethod(get_ctr)


pers = Personne("xxx", "Gichin")
pers.name = "Funakoshi"
print "Nom = ", pers.name

### Lister toutes les attributs et méthodes de la classe ###
print "Tous les objets : " + str(dir(pers))

print "Toutes les méthodes : " + str([methode for methode in dir(pers) if callable(getattr(pers, methode))])

