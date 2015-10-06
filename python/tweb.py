# -*- coding: utf-8 -*-
__author__ = 'lmaignan'

import urllib
import xml.etree.ElementTree as xe
import re


INVALID_TEMP = 32000

#
# Fonction de conversion Kelvin -> Celsius
#

celsius = lambda kelvin : kelvin - 273.15


#
# retourne le contenu d'une page web à partir de son URL
#

def printWebPage(url):

    htmlSource = '<undefined>'

    try:

        sock = urllib.urlopen(url)
        htmlSource = sock.read()
        sock.close()

    except:
        print "Erreur détectée !!!"

    return htmlSource


#
# Récupération d'une température de ville à partir de son ide
#

def getTempCity(id):

    result = printWebPage('http://api.openweathermap.org/data/2.5/weather?id=' + str(id) + '&mode=xml')

    with open('/tmp/weather.xml','w') as f:
        f.write(result)

    try:

        root = xe.parse('/tmp/weather.xml').getroot()
        temp = float(root.findall('temperature')[0].get('value'))

    except xe.ParseError:
        return INVALID_TEMP

    return celsius(temp)



#
# programme principal
#

if __name__ == '__main__':

    dictCity = {}

    with open ('city.FR.json','r') as f:

        for line in f.readlines():

            sre = re.search(r"id\":(?P<id>(\d*)),\"name\":\"(?P<name>(.*))\",\"country",line)
            dictCity[sre.group('name')] = sre.group('id')


    lstCity = dictCity.keys()
    lstCity.sort()

    for name in lstCity:

        temp = getTempCity(dictCity[name])

        if temp != INVALID_TEMP:

            print 'City ', name, ' has temperature of ', getTempCity(dictCity[name]), ' °C'

