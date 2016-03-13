# -*- coding: utf8 -*-
__author__ = 'sbourdin'

from TestsAvecUnittest import Demo

# Pytest remplace Unittest : il crée les tests par introspection du code
# Pour l'installer : pip install pytest
# Pour lancer les tests : py.test <nmodule>.py


demo = Demo(20, 2)


def test_somme():
    assert demo.somme() == 22


def test_difference():
    assert demo.difference() == 18


def test_produit():
    assert demo.produit() == 40


def test_division():
    assert demo.division() ==10

