#insert sort

import random
import time

L =[]
for i in range(10000):
    L.append(i)

random.shuffle(L)

print("length of data: %d" %(len(L)))
current_time = time.time()
#insertion sort assures you that
#if you are at nth iteration, then at least 1 to nth element is sorted!

for i in range(len(L)):
    for j in range(i, 0, -1): #i to 0, decreasing by 1
        if L[j] < L[j-1]:
            L[j], L[j-1] = L[j-1], L[j]
        else:
            break



print("insertion sort time: %s " %(time.time()-current_time))

if sorted(L) == L:
    print("successfully sorted.")
else:
    print("not successful")

# time complexity is 1 + 2+ ..+n-1 =n(n-1)/2 = O(N^2)
