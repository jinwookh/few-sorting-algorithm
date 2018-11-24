#bubble sort

import random
import time

L =[]
for i in range(10000):
    L.append(i)

random.shuffle(L)

print("length of data: %d" %(len(L)))
current_time = time.time()

#bubble sort's feature:
#1. at first iteration, largest number will be most right of array.
#2. so comparing number is going to keep decreased..
#CORE: bubble sort ASSURES you that
#largest number of L[0:N-i] will be at most right of L[0:N-i].
#i: iteration number, N: length of L


for i in range(len(L)):
    for j in range(0, len(L)-1-i):
        if L[j] > L[j + 1]:
            L[j], L[j+1] = L[j+1], L[j]


print("bubble sort time: %s " %(time.time()-current_time))
if sorted(L) == L:
    print("successfully sorted.")
else:
    print("not successful")


#time complexity is n-1+n-2+n-3+ .... + 1 = n(n-1)/2 = O(N^2)

    

