#! /usr/bin/python

from mysql.connector import *
from mysql.connector import errorcode
import sys

def initBD():

        try:
           return connect(user='root',password='root',database='lmpers',host='localhost')
        except Error as err:
           if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print "Pb Username/Password"
                return None
           elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print "Unknown database"
                sys.exit(-1)
           else:
                print err
                sys.exit(-1)



def listAll():

        curs = cnx.cursor()
        curs.execute ('select * from pers')
        for (id, nom, prenom) in curs:
           print 'Id = ' + str(id) + ' Prenom = ' + prenom + ' Nom = ' + nom
        curs.close()

cnx = initBD()

if cnx != None:
        listAll()
        cu= cnx.cursor()
        cu.execute ('insert into pers values (%s,%s,%s)',('4','Said','Touil'))
        cnx.commit()
        cu.close()
        cnx.close()     
