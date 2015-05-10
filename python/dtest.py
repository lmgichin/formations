__author__ = 'Luc Maignan'

import doctest


def somme(a, b):
    """
    ceci est une fonction de somme de deux entiers
    Oui simple mais...
    >>> somme(2,3)
    6
    """

    return a + b

# #######################################################################################

if __name__ == '__main__':
    doctest.testmod()