# -*- coding: utf-8 -*-
__author__ = 'lucio'

import pickle
import json


class Personne:

    def __init__(self, nom, prenom):

        self.nom, self.prenom = nom, prenom



def save_pickle():

    l_p = [p1, p2, p3]

    with open('pickleTest','wb') as f:
        pickle.dump(l_p, f)


def load_pickle():

    with open('pickleTest','rb') as f:
        ld = pickle.load(f)

    return ld


def save_json():

    l = list()
    l.append([{'nom': p1.nom, 'prenom' : p1.prenom}, {'nom': p2.nom, 'prenom' : p2.prenom}, {'nom': p3.nom, 'prenom' : p3.prenom}])

    with open('jsonTest', 'w') as f:
        json.dump(l, f, indent=3)


def read_json():

        with open('jsonTest', 'r') as f:
            j = json.load(f)

        return j


p1 = Personne('Hugo','Victor')
p2 = Personne('Verlaine','Paul')
p3 = Personne('Camus','Albert')


save_pickle()
print "Results from pickle : ", load_pickle()

save_json()
print "Results from json : ", read_json()