# -*- coding: utf-8 -*-

def menu():

    print "1 - Saisie"
    print "2 - Suppression par indice"
    print "3 - Suppression par valeur"
    print "4 - Affichage"
    print "5 - Sortie"


def saisie():

    lst.append(int(raw_input("Valeur ?")))

def affiche():

    for it in lst:
        print "Elément = ", it

def supval():

    valeur = int(raw_input("Valeur ?"))

    if valeur in lst:
        lst.remove(valeur)

choix = 0
lst = []

while choix != 5:

    menu()
    choix = int (raw_input("Choix ?"))

    if choix == 1:
       saisie()
    elif choix == 3:
        supval()
    elif choix == 4:
        affiche()
