#!/usr/bin/python
import timeit
# ###########################################################################################################

def fibo(n):
	a, b = 0, 1
	for i in range(n):
		a, b = b, a+b

	return a

# ###########################################################################################################

def fibo_r(n):

	if n in (0,1):
	  return n;
	
	return fibo_r(n-2) + fibo_r(n-1)

# ###########################################################################################################

def affiche():

    for j,i in enumerate(xrange(10)):
        print 'rang {} = {}'.format(j+1,fibo(i))


print timeit.timeit(stmt="affiche()",setup="from __main__ import affiche",number=1)

def genfib():

    i = 0

    while True:
        yield fibo_r(i)
        i += 1


for i,j in enumerate(genfib()):

    if i == 25:
        break
    else:
        print j

