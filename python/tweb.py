# -*- coding: utf-8 -*-
__author__ = 'lmaignan'

import urllib
import xml.etree.ElementTree as xe
import re


INVALID_TEMP = 32000
APPID= "8243d32f720393b112cde963b4a4ac60"
WEATHER_URL="http://api.openweathermap.org/data/2.5/weather?id={id}&mode=xml&APPID={appid}"
WEATHER_XML="/tmp/weather.xml"
CITY_FILE="city.FR.json"

#
# Fonction de conversion Kelvin -> Celsius
#

celsius = lambda kelvin: kelvin - 273.15


#
# retourne le contenu d'une page web à partir de son URL
#

def get_web_page(url):

    htmlSource = '<undefined>'

    try:

        sock = urllib.urlopen(url)
        htmlSource = sock.read()
        sock.close()

    except:
        print "Erreur détectée !!!"

    return htmlSource


#
# Récupération d'une température de ville à partir de son id
#

def get_temp_city(id):

    result = get_web_page(WEATHER_URL.format(id=id,appid=APPID))

    with open(WEATHER_XML,'w') as f:
        f.write(result)

    try:

        root = xe.parse(WEATHER_XML).getroot()
        temp = float(root.findall('temperature')[0].get('value'))

    except xe.ParseError:
        return INVALID_TEMP

    return celsius(temp)



#
# programme principal
#

if __name__ == '__main__':

    dictCity = {}
    expr = re.compile(r"id\":(?P<id>(\d*)),\"name\":\"(?P<name>(.*))\",\"country")

    with open (CITY_FILE,'r') as f:

        for line in f.readlines():

            sre = re.search(expr,line)
            dictCity[sre.group('name')] = sre.group('id')


    lstCity = dictCity.keys()
    lstCity.sort()

    for name in lstCity:

        temp = get_temp_city(dictCity[name])

        if temp != INVALID_TEMP:

            print 'City ', name, ' has temperature of ', temp, ' °C'

