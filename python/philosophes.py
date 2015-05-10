# -*- coding: utf-8 -*-

import threading
import time
import random


class Philosophe(threading.Thread):

    tempsRepas = 2
    couverts = None

    def __init__(self, nom):
        self.nom = nom
        self.compteur = 0
        if Philosophe.couverts is None:
            Philosophe.couverts = threading.Lock()
        threading.Thread.__init__(self)

    def attendreCouverts(self):
        while not Philosophe.couverts.acquire(False):
            self.reflechir()
            time.sleep(0.2)

    def rendreCouverts(self):
        Philosophe.couverts.release()

    def reflechir(self):
        print(self.nom + " réfléchit\n")

    def manger(self):
        time.sleep(0.5)
        self.attendreCouverts()
        self.compteur = self.compteur + 1
        print(self.nom + " mange son repas " + str(self.compteur) + "\n")
        time.sleep(Philosophe.tempsRepas)
        self.rendreCouverts()

    def run(self):
        
        while self.compteur < 5:
            self.reflechir()
            self.manger()
            time.sleep(0.5)

        print(self.nom + " se retire\n")











lsPhi=[]

for i in range(7):
    lsPhi += [ Philosophe("Philosophe n° {}".format(i))]


random.shuffle (lsPhi)

for philo in lsPhi:
    philo.start()

for philo in lsPhi:
    philo.join()

print "Fini pour les philosophes!"






















