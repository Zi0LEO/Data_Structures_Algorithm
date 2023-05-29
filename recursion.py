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

def permute(A, k):
    if k == len(A):                         #O(1)
        global h                            #O(1)
        h += 1                              #O(1)
        print(h, ") ", A)                   #O(1)
    else:
        for i in range(k, len(A)):          #O(n - k)
            A[k], A[i] = A[i], A[k]         #O(1)
            permute(A, k + 1)               #Tpermute(n) = O(1) + O(n) + n * Tpermute(n - 1), è ovviamente un fattoriale, dimostrare per induzione
            A[k], A[i] = A[i], A[k]         #O(1)

#Tpermute(n) = O(n!)
#Spermute(n) = O(n)


def riduci(M, i):
    C = []
    print(M)
    for j in range(1, len(M)):
        copy = M[j]
        C.append(copy.pop(i))
    return C

def det(M):
    if len(M) == 1:                         #O(1)
        return M[0][0]                      #O(1)
    d = float(0)                            #O(1)
    for i in range(len(M)):                 #n * O(1)
        C = riduci(M, i)                    #n * O(n^2)
        d += pow(-1, i) * M[0][i] * det(C)  #n * O(1) + Tdet(n-1)
    return d                                #O(1)


A = [[1, -4, 2], [3, 1, -6], [1, -1, -1]]
print(det(A))