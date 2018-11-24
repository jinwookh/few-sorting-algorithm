#merge sort
import random
import time


def mergeSort(L, a, b):
     #use recursive call
     #use devide and conquer algorithm
     c = (b-a)//2 + a
     
     if b-a < 0:
          print('error occured! 3rd parameter is smaller than 2nd one')
     if b-a == 0:
          return
     elif b-a == 1:
          if L[b] < L[a]:
               L[b], L[a] = L[a], L[b]
               #above code was trouble
               #L[b], L[a] = L[b] , L[a] which was foolish..
          return

     
     mergeSort(L, a, c)
     mergeSort(L, c+1, b)
     merge (L, a,c+1, b)
     C = L[a:b].copy()
     


def merge(L, a, startb, b):
     #MERGE space is needed.
     #everytime this function is called, size of b-a space is needed
     S = L[a:startb].copy()
     
     T = []
     M = []
     if (b == startb):
          T.append(L[b])
     else:
          T = L[startb:(b+1)].copy()
     
     i = 0
     j = 0
     while(i < len(S)) and (j < len(T)):
          if S[i] < T[j]:
               M.append(S[i])
               i = i+1
          else:
               M.append(T[j])
               j = j+1

     if i <len(S):
          M = M + S[i:]
     if j < len(T):
          M = M + T[j:]
     
     L[a:(b+1)] = M
     
     

L = []
for i in range(1000000):
     L.append(i)
A = L.copy()
random.shuffle(A)


print("length of data: %d" %(len(L)))          
starttime = time.time()
mergeSort(A, 0, len(A)-1)
print("mergesort time: %s" %(time.time()-starttime))
if sorted(A) == A:
     print("merge algorithm successfully sorted!")
else:
     print("merge algorithm failed")

#backlash: uses stack because of recursive call, need additional space to place merged sublist

