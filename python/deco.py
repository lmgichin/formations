# -*- coding: utf-8 -*-

__author__ = 'lucio'

# ######################################################################################################################
# sample de tests des fonctions décorées en python
# ######################################################################################################################


# ######################################################################################################################
# fonction servant de décorateur d'une fonction sans paramètres
# ######################################################################################################################

def basic_deco(func):

    def wrapper():
        return func()

    print "Dans la fonction décorée (exécuté automatiquement une fois)"

    return wrapper

# ######################################################################################################################
# test de décoration sans paramètres
# ######################################################################################################################


@basic_deco
def code_func():
    """
    Ceci est la documentation de la fonction codée
    """
    print "Code dans la fonction"


# ######################################################################################################################
# fonction servant de décorateur d'une fonction avec  paramètres
# ######################################################################################################################


def args_deco(func):

    def deco_wrapper(arg1, arg2):

        print "interception de la personne {} {}".format(arg1,arg2)
        return func(arg1,arg2)

    return deco_wrapper

# ######################################################################################################################
# test de décoration avec paramètres
# ######################################################################################################################


@args_deco
def print_nom(nom, prenom):

    print "Je m'appelle {} {}".format(nom, prenom)

# ######################################################################################################################
# fonction servant de décorateur avec paramètres d'une fonction avec  paramètres
# ######################################################################################################################


def args_deco_args(da1, da2):

    def mdeco(func):

        def mwrap(fa1, fa2):

            print "Arguments du décorateur : {} {}".format(da1,da2)
            print "Arguments de la fonction {} {}".format(fa1,fa2)

            return func(fa1,fa2)

        return mwrap

    return mdeco

# ######################################################################################################################
# test de décoration avec paramètres
# ######################################################################################################################


@args_deco_args('Deco Arg1', 'Deco Arg2')
def print_nom_param(nom, prenom):

    print "Je m'appelle {} {}".format(nom, prenom)


# ######################################################################################################################
# fonction de décoration comptant le nombre d'appels à une fonction
# ######################################################################################################################

def func_counter(func):

    def wrapper(*args, **kwargs):

        wrapper.count = wrapper.count + 1
        print "Appel #{} de la fonction {}".format(wrapper.count, func.__name__)

        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper

# ######################################################################################################################
# test de nomre d'appels d'une fonction
# ######################################################################################################################


@func_counter
def fcount():
    pass

@func_counter
def fcount2():
    pass

# ######################################################################################################################
# fonction de décoration mesurant le temps d'exécution d'une fonction
# ######################################################################################################################


def func_time(func):

    import time

    def wrapper(*args, **kwargs):

        t = time.clock()
        res = func(*args, **kwargs)
        print "Exécution de {} : {}".format(func.__name__, time.clock()-t)

        return res

    return wrapper

# ######################################################################################################################
# test de mesure du temps d'exécution
# ######################################################################################################################

@func_time
def f():

    j = 0

    for i in range(10000):
        j = i + 1


# ######################################################################################################################
# le main...
# ######################################################################################################################

if __name__ == '__main__':

    print '\nProgramme de test de fonctions décorées\n'
    code_func()
    f()
    f()
    fcount()
    fcount()
    fcount2()
    fcount2()
    fcount2()
    print "Fonction fcount appelée {} fois, et fcount2 {} fois".format(fcount.count, fcount2.count)
    print_nom('Funakoshi','Gichin')
    print_nom_param('Funakoshi','Gichin')
