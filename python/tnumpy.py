# -*- coding: utf-8 -*-

__author__ = 'Luc Maignan'

import time
import numpy as np


def trad_version():

    t1 = time.time()
    X = range(10000000)
    Y = range(10000000)
    Z = []

    for idx, i in enumerate(X):
        Z.append(X[idx] + Y[idx])

    return time.time() - t1


def numpy_version():

    t1 = time.time()
    X = np.arange(10000000)
    Y = np.arange(10000000)
    Z = X + Y

    return time.time() - t1


def array_numpy():

    a = np.array([[1, 2, 3, 4], [4, 5, 6, 7]], int)
    a[0, 0] = 0
    print "Array  =", a
    print "Dimension = ", a.shape, " Longueur = ", len(a)
    print "Type = ", a.dtype
    a = a.reshape((4, 2))
    print a
    a = a.flatten()
    print a

    print np.arange(10, dtype=np.uint32)


def resolve_equation(coeff, values):



    return 0, 0, 0

# ####################################################################################################

if __name__ == '__main__':

    print "Temps d'exécution de la version traditionnelle : ", trad_version()
    print "Temps d'exécution de la version numpy : ", numpy_version()
    array_numpy()

    # resoudre
    #     x + y + z = 3
    #     x + 2y + 3z = 0
    #     x + 3y + 4z = -2

    print "Résultat = ", resolve_equation(np.matrix('1,1,1;,1,2,3;,1,3,4'), np.matrix('3,0,-2'))