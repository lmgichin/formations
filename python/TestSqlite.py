# Encoding: UTF-8

__author__ = 'lmaignan'

import sqlite3 as sql



print "Version driver : {}".format(sql.version)

print "Connexion à la base...",
conn = sql.connect(':memory:')
print "OK" if conn is not None else "KO"

print "Création de la tables PERSONNE..."
curs = conn.cursor()
curs.execute("CREATE TABLE PERSONNE (PERS_ID INTEGER PRIMARY KEY, PERS_NOM VARCHAR(50), PERS_PRENOM VARCHAR(50))")
print "insert data"
curs.execute("INSERT INTO PERSONNE (PERS_NOM,PERS_PRENOM) VALUES (?,?)", ("MAIGNAN", "Luc"))
curs.execute("INSERT INTO PERSONNE (PERS_NOM,PERS_PRENOM) VALUES (?,?)", ("BOURDIN", u"Stéphane"))
print "get data..."

for nom, prenom in curs.execute('Select PERS_NOM, PERS_PRENOM From PERSONNE'):
    print u"Nom : {}, Prenom : {}".format(nom, prenom)

curs.close()

conn.commit()
conn.close()
