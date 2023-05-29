def sum(A, i):
    if i >= len(A):                     #O(1)
        return 0                        #O(1)
    else:
        return A[i] + sum(A, i + 1)     #O(1) * Tsum()
    
#Tsum = O(n)
#Ssum = O(n)

def prodScalRec(A, B, k):
    if k < 0:
        return 0
    else:
        return prodScalRec(A,B, k - 1) + A[k] * B[k]
    
#TprodScalRec = O(n)
#SprodScalRec = O(n)


def sumVectRec(A, B, k):
    if k < 0:
        return []
    else:
        C = sumVectRec(A, B, k-1)
        C.append(A[k] + B[k])
        return C

#TsumVectRec = O(n)
#SsumVectRec = O(n)


def sumMatRec(A,B,i):
    if i < 0:                           #O(1)
        return []                       #O(1)
    else:
        L = sumVectRec(A[i], B[i], k)   #O(k)
        C = sumMatRec(A, B, i-1)        #O(i)
        C.append(L)                     #O(1)
        return C                        #O(1)
    
#TsumMatRec = O(n * i)
#SsumMatRec = O(n * i)