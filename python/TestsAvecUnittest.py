# -*- coding: utf8 -*-
# __author__ = 'sbourdin'

# Unittest est le module de tests Python par défaut
# pour l'utiliser, il faut importer le module unittest
# Pour lancer les tests : python -m unittest <nommodule> (automatique sous pycharm)

import unittest


class Demo:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def somme(self):
        return self.a + self.b

    def difference(self):
        return self.a - self.b

    def produit(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b


# La classe de test doit hérité de unittest.TestCase

class TestDemo(unittest.TestCase):
    def __init__(self, methodname="runTest"):
        unittest.TestCase.__init__(self, methodname)
        self.demo = Demo(20, 2)

    # Toutes les fonctions de tests doivent commencer par "test"

    def test_somme(self):
        self.assertEqual(self.demo.somme(), 22)

    def test_difference(self):
        self.assertEqual(self.demo.difference(), 18)

    def test_produit(self):
        self.assertEqual(self.demo.produit(), 40)

    def test_division(self):
        self.assertEqual(self.demo.division(), 10)

