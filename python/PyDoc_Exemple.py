# -*- coding: utf8 -*-
__author__ = 'sbourdin'


def unefonction():
    """Ceci est une 'doc string' ou 'chaine de documentation' qui permet de décrire
    ce que fait la fonction et la valeur retounée.
    Il est possible de générer un squelette de docstring en déclenchant ALT RETURN
    sur le corps d'une fonction et méthode et en sélectionnant "Insert documentation string stub".
    D'après la norme, il ne doit pas y avoir de lignes vides avant et après la doc string.
    Cette fonction de test renvoie une chaine Hello World !
    """
    return "Hello World !"


def uneautrefonction(a, b):
    """
    Cette fonction permet de faire une somme.
    :param a: int
    :param b: int 
    :rtype: int
    :return: la somme des deux paramètres
    """
    return a + b


class Uneclasse:

    def __init__(self, nom, prenom):
        """
        Construteur principal
        :param nom: string
        :param prenom: string
        """
        self.nom = nom
        self.prenom = prenom

    def __str__(self):
        """

        :type self: object
        """
        return self.prenom + " " + self.nom

    def unemethode(self):
        return "Le nom de la personne est " + str(self)
