#quick sort
#ASSURES you that if you choose one number to be pivot,
#that number would be at right spot
#compared index is keep getting closer to pivot
#use devide and conquer algorithm

def quick_sort(L, a, b):
    pivot = a
    compared = b


    if b > a:
        while pivot != compared :
            
            if pivot < compared:
                if L[pivot] > L[compared]:
                    L[pivot], L[compared] = L[compared], L[pivot]
                    pivot, compared = compared, pivot
                    compared = compared + 1
                else:   
                    compared = compared -1
            else:
                if L[pivot] < L[compared]:
                    L[pivot], L[compared] = L[compared], L[pivot]
                    pivot, compared = compared, pivot
                    compared = compared - 1
                else:   
                    compared = compared + 1
            
        
        quick_sort(L, a, pivot)
        quick_sort(L, pivot+1, b)

import random
import time

L = []
for i in range(10000000):
     L.append(i)
A = L.copy()
random.shuffle(A)

print("length of data: %d" %(len(L)))          
starttime = time.time()
quick_sort(A, 0, len(A)-1)

print("quicksort time: %s" %(time.time()-starttime))
if sorted(A) == A:
     print("quick algorithm successfully sorted!")
else:
     print("quick algorithm failed")

     
