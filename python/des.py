# coding=utf-8
__author__ = 'lmaignan'

import random
from itertools import *

# ##################################################################################################
# génération à arguments variables des tirages pour chaque joueur
# ##################################################################################################

def genVarVal(*args, **kwargs):

    dico = {}

    for joueur in args:

        lstTir = []

        for i in range(kwargs['nbTirages']):

              lstTir += [tuple  ( imap ( lambda x: random.randrange(1,7), range(kwargs['nbDes']) ) )  ]

        dico[joueur] = tuple ( lstTir )


    return dico

# ##################################################################################################
# génération à arguments fixes des tirages pour chaque joueur
# ##################################################################################################

def genFixedVal(lstJoueurs,nbTirages=6, nbDes=4):

    dico = {}

    for joueur in lstJoueurs:

        lstTir = []

        for i in range(nbTirages):

            lstTir += [tuple ( imap ( lambda x: random.randrange(1,7), range(nbDes) ) )  ]

        dico[joueur] = tuple(lstTir)


    return dico

# ##################################################################################################
# génération d'un dictionnaire avec le nombre de valeurs identiques par joueur
# ##################################################################################################


def getDoubles(dico):

    dicoRes = {}

    for joueur in dico.keys():

        cpt = 0

        for tirage in dico[joueur]:

            val0 = tirage[0]

            for indice,valeur in enumerate(tirage):

                if valeur != val0:
                    break
            else:
                cpt +=1

        dicoRes[joueur] = cpt

    return dicoRes

# ##################################################################################################
# génération d'un dictionnaire avec les stats de valeurs par joueur
# ##################################################################################################


def getStats(dico):

    dicoRes = {}

    for joueur in dico.keys():

        dVal = {}

        for tirage in dico[joueur]:

            for tir in enumerate(tirage):
                dVal[tir[1]] = dVal.get(tir[1],0) + 1

        dicoRes[joueur] = dVal

    return dicoRes


# ##################################################################################################
# le main...
# ##################################################################################################

if __name__ == '__main__':

    lstJoueurs = ['LMA', 'SBO']
    dct = genFixedVal(lstJoueurs, nbDes=2)
    #dct = genVarVal('LMA','SBO', 'JWU', nbTirages=3, nbDes=3)
    print "Tirages = ", dct
    print "Doubles = ", getDoubles(dct)
    print "Statts = ",getStats(dct)
