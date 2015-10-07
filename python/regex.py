# -*- coding: UTF-8 -*-
__author__ = 'Luc Maignan'


import re

chaine = ""

expression = r"^0[0-9]([ .-]?[0-9]{2}){4}$"

#while re.search(expression, chaine) is None:

#    chaine = raw_input("Saisissez un numéro de téléphone (valide) :")


print "Chaîne remplacée : ", re.sub(r"(.*) (.*)",r"\2 \1","Nom Prénom")


line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print "matchObj.group() : ", matchObj.group()
   print "matchObj.group(1) : ", matchObj.group(1)
   print "matchObj.group(2) : ", matchObj.group(2)
else:
   print "No match!!"

searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
   print "searchObj.group() : ", searchObj.group()
   print "searchObj.group(1) : ", searchObj.group(1)
   print "searchObj.group(2) : ", searchObj.group(2)
else:
   print "Nothing found!!"

print ''


matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print "match --> matchObj.group() : ", matchObj.group()
else:
   print "No match!!"

searchObj = re.search( r'dogs', line, re.M|re.I)
if searchObj:
   print "search --> searchObj.group() : ", searchObj.group()
else:
   print "Nothing found!!"