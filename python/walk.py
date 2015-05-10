# -*- coding: utf-8 -*-
__author__ = 'Luc Maignan'

import os


def liste(directory):

    for racine, repertoire, fichiers in os.walk(directory):

        print "Répertoire : " + racine

        for rep in repertoire :
            print '---' + os.path.join(directory,rep)

        print "Fichiers de " + racine

        for fic in fichiers :
            print '---' + fic

# ########################################################################################################

if __name__ == '__main__':

    if os.name == 'posix':
        ndir = '/tmp'
    else:
        ndir = 'c:\\temp'

    liste(ndir)

