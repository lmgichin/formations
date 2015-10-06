# -*- coding: utf-8 -*-
__author__ = 'lmaignan'

import urllib
import xml.etree.ElementTree as xe

celsius = lambda kelvin : kelvin - 273.15

def printWebPage(url):

    htmlSource = '<undefined>'

    try:

        sock = urllib.urlopen(url)
        htmlSource = sock.read()
        sock.close()

    except:
        print "Erreur détectée !!!"

    return htmlSource

# printWebPage('http://ipv4bot.whatismyipaddress.com')

def getTempCity(id):

    result = printWebPage('http://api.openweathermap.org/data/2.5/weather?id='+str(id)+'&mode=xml')

    with open('/tmp/weather.xml','w') as f:
        f.write(result)

    root = xe.parse('/tmp/weather.xml').getroot()
    temp = float(root.findall('temperature')[0].get('value'))

    return celsius(temp)

print getTempCity(6455259)

