from random import *

nombre, val, essai =  int(10 * random()), -1, 0

while val != nombre:

    val = int ( raw_input("Nombre ?"))
    essai += 1

    if val > nombre:
        print "Trop grand"
    elif val < nombre:
        print "Trop petit"

else:
    print "Nbre essais = ", essai