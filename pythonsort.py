#python sorted method
import random
import time

L =[]
for i in range(10000000):
    L.append(i)

random.shuffle(L)
print("length of data: %d" %(len(L)))
current_time = time.time()
L.sort()
print("python sort function time: %s " %(time.time()-current_time))
