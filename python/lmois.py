# -*- coding: utf-8 -*-

lmois = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet',
         'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']]
ljour = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi','Dimanche']


nj = 0

for idx, mois in enumerate(lmois[1]):

    for jour in range(1, lmois[0][idx] + 1):

        print ljour[nj], jour, mois
        nj = (nj +1) % 7