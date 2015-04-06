# -*- coding: utf-8 -*-
__author__ = 'lucio'


import ZODB, ZODB.FileStorage

database = raw_input('Entrez le nom de la base : ')
objet = raw_input("Entrez le nom de l'objet à dumper : ")

storage = ZODB.FileStorage.FileStorage(database)
db = ZODB.DB(storage)
conx = db.open()
root = conx.root()

try:

    print root[objet]

except KeyError:

    print "clé non trouvée !"
    print root.items()

finally:

    db.close()