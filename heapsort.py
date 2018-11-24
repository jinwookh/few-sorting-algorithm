#heap sort
import random
import time

L = []
for i in range(1000000):
     L.append(i)
A = L.copy()
random.shuffle(A)

print("length of data: %d" %(len(L)))          
starttime = time.time()



H = [] #heap list
H.append(-1) #set H[0] as non-used seat
S = [] #sorted list

for i in range(len(A)):
    H.append(A[i])
    j = i + 1
    while j != 1:
        k = j // 2
        if H[j] < H[k]:
            H[j], H[k] = H[k], H[j]
            j = k
        else:
            break
# above code is about inserting elements into heap

        


while 1:
    
    
    if len(H) > 2:
        S.append(H[1])
        H[1] = H.pop()
    else:
        S.append(H.pop())
        break
    j = 1
    while 1:
        k = j * 2
        
        if k >= len(H):
            break
        elif k+1 == len(H):
            if H[k] < H[j]:
                H[k], H[j] = H[j], H[k]
            break
        
        if H[k] < H[k+1]:
            if H[k] < H[j]:
                H[k], H[j] = H[j], H[k]
                j = k
            else:
                break
        else:
            if H[k + 1] < H[j]:
                H[k+1], H[j] = H[j], H[k+1]
                j = k+1
            else:
                break

    #above is heap deletion code


print("heap sort time: %s" %(time.time()-starttime))
if sorted(A) == S:
     print("heap algorithm successfully sorted!")
else:
     print("heap algorithm failed")
     
#backlash: storage for heap is needed
