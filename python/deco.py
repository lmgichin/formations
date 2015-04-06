# -*- coding: utf-8 -*-

from functools import wraps

__author__ = 'lucio'

# ######################################################################################################################

def basic_deco(func):

    def wrapper():
        return func()

    print "Dans la fonction décorée"

    return wrapper

@basic_deco
def code_func():
    """
    Ceci est la documentation de la fonction codée
    """
    print "Code dans la fonction"


def args_deco(func):

    def deco_wrapper(arg1, arg2):

        print "interception de la personne {} {}".format(arg1,arg2)
        return func(arg1,arg2)

    return deco_wrapper

@args_deco
def print_nom(nom,prenom):

    print "Je m'appelle {} {}".format(nom,prenom)


def args_deco_args(da1, da2):

    print "Arguments du décorateur : {} {}".format(da1,da2)

    def mdeco(func):

        def mwrap(fa1, fa2):

            print "Arguments de la fonction {} {}".format(fa1,fa2)

            return func(fa1,fa2)

        return mwrap

    return mdeco


def func_counter(func):

    def wrapper(*args, **kwargs):

        wrapper.count = wrapper.count + 1
        print "Appel #{} de la fonction {}".format(wrapper.count, func.__name__)

        return func(*args, **kwargs)

    print 'toto'
    wrapper.count = 0
    return wrapper

def func_time(func):

    import time

    def wrapper(*args, **kwargs):

        t = time.clock()
        res = func(*args, **kwargs)
        print "Exécution de {} : {}".format(func.__name__, time.clock()-t)

        return res

    return wrapper

@func_time
def f(a1):
    return a1

class Point:

    def __init__(self,x):
        self.x = x

    @property
    def x(self):
        return self.x

    @x.setter
    def x(self,val):
        self.x = val

print 'Ma fct = ',f(14)
p = Point(3)

print p.x
p.x =7
print p.x