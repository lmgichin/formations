# -*- coding: utf-8

__author__ = 'Luc Maignan'

import subprocess
import os
import re


host = 'free.fr'

if os.name == 'posix':
    pcount = '-c'
else:
    pcount = '-n'

pr = subprocess.Popen(['ping', pcount, '2', host], stdout=subprocess.PIPE)

output = pr.communicate()[0]

try:

    if os.name == 'posix':

        perte = re.search(r"(\d*)% packet loss", output).groups()
        print "% de perte de paquets = " + perte[0]
        temps = re.search(r"min/avg/max.* = (\d*\.\d*)/.*/(\d*\.\d*)/", output).groups()
        print "Temps minimal = {0[0]} ms, Temps maximal = {0[1]} ms".format(temps)
        ip = re.search(r"PING .* \((?P<ip>(\d*\.){3}\d*)", output).group('ip')
        print 'IP pingée = ' + ip

    else:
        perte = re.search(r"perte (\d*)", output).groups()
        print "% de perte de paquets = " + perte[0]
        temps = re.search(r"Minimum = (\d*).*Maximum = (\d*)", output).groups()
        print "Temps minimal = {0[0]} ms, Temps maximal = {0[1]} ms".format(temps)
        ip = re.search(r"pour (?P<ip>.*):", output).group('ip')
        print 'IP pingée = ' + ip

except AttributeError:
    print "La requête n'a rien retourné !"
    print "Debug = ", output