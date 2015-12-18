__author__ = 'lmaignan'

import thread
import threading
import time
import random

def mylt():

    for i in range(1,10):
        time.sleep(2)
        print i

t=thread.start_new_thread(mylt,())
print 'fin'



















class MyThread(threading.Thread):
    def run(self):
        print "{} started !".format(self.getName())
        time.sleep(1)
        print "{} finished !".format(self.getName())

lt=[]
for x in range(4):
    lt+=[MyThread(name="Thread-{}".format(x+1))]
#
# random.shuffle(lt)

for x in lt:
    x.start()



for x in lt:
    x.join()