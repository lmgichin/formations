# -*- coding: UTF-8 -*-
__author__ = 'Luc Maignan'



MFILE = '/tmp/mfile.data'


with open(MFILE, 'w') as f:
    f.write('Line 1\n')
    f.write('Line 2\n')
    f.write('Line 3\n')
    f.write('ça va ?\n')


with open(MFILE, 'r') as f:

    for line in f.readlines():
        print line,