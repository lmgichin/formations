# -*- coding: utf-8 -*-
__author__ = 'lucio'


import ZODB, ZODB.FileStorage, persistent, transaction
from BTrees.OOBTree import OOBTree


# #########################################################################################################
# les classes de test ...
# #########################################################################################################

class Personne(persistent.Persistent):

    def __init__(self, nom):
        self.nom = nom


    def get_attr(self):
        return self.nom


class PersPhys(Personne):

    def __init__(self, nom, prenom):

        Personne.__init__(self,nom)
        self.prenom = prenom

    def get_nom(self):

        return self.nom

    def get_prenom(self):

        return self.prenom

    def get_attr(self):

        return Personne.get_attr(self), self.prenom

    def __str__(self):

        return "Description Personne Physique : " + str(self.get_attr())


# #########################################################################################################
# Allez on teste tout ça...
# #########################################################################################################


def store():

    print "Saisie d'une personne..."
    nom = raw_input("Nom : ")
    prenom = raw_input("Prenom : ")

    listePersonnes['PersonnesPhysiques'] += [ PersPhys(nom,prenom) ]
    root['Personnes'] = listePersonnes

    transaction.commit()


# #######################################################################################################
# impression de la liste des personnes
# #######################################################################################################

def get():

    print "Liste des personnes : \n"

    for i in listePersonnes['PersonnesPhysiques']:
        print i


# #######################################################################################################
# recherche d'une personne
# #######################################################################################################

def get_pers(nom, prenom):

    for it in listePersonnes['PersonnesPhysiques']:

        if it.get_nom() == nom and it.get_prenom() == prenom:
            return it
    else:
        return None

# #######################################################################################################
# suppression d'une personne
# #######################################################################################################

def delete():

    nom = raw_input("Nom : ")
    prenom = raw_input("Prenom : ")
    pers = get_pers(nom, prenom)

    if pers is not None:

        listePersonnes['PersonnesPhysiques'].remove(pers)
        root['Personnes'] = listePersonnes
        transaction.commit()

    else:
        print "Personne non trouvée"

# #######################################################################################################
# mise à jour d'une personne
# #######################################################################################################

def update():

    nom = raw_input("Nom : ")
    prenom = raw_input("Prenom : ")
    pers = get_pers(nom, prenom)

    if pers is not None:

        new_nom = raw_input("Nouveau Nom : ")
        new_prenom = raw_input("Nouveau Prenom : ")
        pers.nom = new_nom
        pers.prenom = new_prenom
        root['Personnes'] = listePersonnes
        transaction.commit()

    else:
        print "Personne non trouvée"

# ###########################################################################
# main ...
# ###########################################################################

storage = ZODB.FileStorage.FileStorage('testZODB-bt')
db = ZODB.DB(storage)
conx = db.open()
root = conx.root()

choix = 0

listePersonnes = root.get('Personnes',OOBTree())

if not listePersonnes.has_key('PersonnesPhysiques'):
    listePersonnes['PersonnesPhysiques'] = []

while choix != 5:

    print "\n1 - Ajouter une personne"
    print "2 - Supprimer une personne"
    print "3 - Modifier une personne"
    print "4 - Lister les personnes"
    print '5 - Sortir\n'

    choix = int ( raw_input ('Votre choix : '))

    if choix == 1:

        store()

    elif choix == 2:

        delete()

    elif choix == 3:

        update()

    elif choix == 4:

        get()

transaction.commit()
conx.close()

