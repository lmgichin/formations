__author__ = 'Luc Maignan'

import doctest

def somme(a, b):
    """
    ceci est une fonction de somme de deux entiers
    Oui simple mais...
    >>> somme(2,3)
    4
    >>> somme(0,0)
    0
    """

    return a + b

def soustraction(a,b):
    """
    ceci est une fonction de soustraction de deux entiers
    Oui simple mais...
    >>> soustraction(2,3)
    -1
    """

    return a - b
# #######################################################################################


doctest.testmod()