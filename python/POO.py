# -*- coding: utf8 -*-


class Personne:
    """
    Classe personne pour la formation
    """

    # Pas de surcharge
    # Pas de polymorphisme direct

    ### Attributs statiques de classe ###
    ctr = 0
    nom = "TOTO"

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
        # Attribut privé
        self.__attribut_prive = 25

    ### Destructeur ###
    def __del__(self):
        pass

    ### Méthode sollicitée par str ###
    def __str__(self):
        return self.prenom + " " + self.nom

    ### Surcharge de l'opérateur + ###
    def __add__(self, objet):
        return Personne(self.nom + " " + objet.nom, self.prenom + " " + objet.prenom)

    ### Méthode privée ###
    def __methode_privee(self):
        return "Méthode privée"

    ### Méthode statique ###
    @staticmethod
    def get_ctr():
        return Personne.ctr


    ### Méthode de classe ##
    @classmethod
    def get_ctr_classe(cls):
        return cls.ctr

    @classmethod
    def renvoie_methodes(cls):
        return [methode for methode in dir(cls)]


    @classmethod
    def aide(cls):
        help(cls)


class Employe(Personne):

    def __init__(self, nom, prenom, date_entree):
        Personne.__init__(self, nom, prenom)
        self.date_entree = date_entree

    def __str__(self):
        return Personne.__str__(self) + " " + self.date_entree


pers1 = Personne("Maignan", "Luc")
print "Personne                             : " + str(pers1)
print "Nombre de personnes                  : " + str(pers1.get_ctr())
print "Nombre de pers (par méth. de classe) : " + str(Personne.get_ctr_classe())

print "Attribut nom de l'instance : " + pers1.nom
print "Attribut nom de la classe  : " + Personne.nom

pers2 = Personne("Bourdin", "Stéphane")
print "Personne : " + str(pers2)
print "Nombre de personnes : " + str(pers2.get_ctr())

print "Concaténation : " + str(pers1 + pers2)

pers3 = Employe("Touil", "Saïd", "01/01/2000")
print "Personne : " + str(pers3)
print "Nombre de personnes : " + str(pers3.get_ctr())

print "Liste des méthodes de la classe      : " + str(Personne.renvoie_methodes())
print "Chaine de documentation de la classe : "
Personne.aide()