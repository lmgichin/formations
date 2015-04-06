__author__ = 'lucio'


class LmWith:

    def __init__(self, param):

        print "Init param = {}".format(param)
        pass

    def __enter__(self):

        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        print "Exit : ", exc_type, exc_val, exc_tb
        pass


with LmWith('Param init') as i:
    raise TypeError('Mauvais type')
    pass
