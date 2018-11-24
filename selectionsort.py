#SELECTION sort

import random
import time

L =[]
for i in range(10000):
    L.append(i)

random.shuffle(L)


print("length of data: %d" %(len(L)))
current_time = time.time()

#selection sort ASSURES you that
#at 1st iteration, 1st smallest will be on the most left seat.(1st seat)
#so at nth iteration, nth smallest will be on the nth seat. ex) 3rd smallest on 3rd seat.

for i in range(len(L)):
    for j in range( i,len(L)):
        if L[i]> L[j]:
            L[i], L[j] = L[j], L[i]




print("selection sort time: %s " %(time.time()-current_time))


if sorted(L) == L:
    print("successfully sorted.")
else:
    print("not successful")

# time complexity is 1 + 2+3+...+n = n(n - 1) /2 = O(n^2)
