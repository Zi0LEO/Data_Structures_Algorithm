def somma(A):
    n = len(A)                  #O(1)
    ret = 0                     #O(1)
    for i in range(n):          #O(n)
        ret += A[i]             #O(1) * n
    return ret                  #O(1)

#Tsomma = O(n)
#Ssomma = O(1)


def sommaVett(A,B):
    C = []                      #O(1)
    for i in range(len(A)):     #O(n)
        C.append(A[i] + B[i])   #O(1) * n
    return C                    #O(1)

#TsommaVett = O(n)
#SsommaVett = O(n)


def prodScal(A,B):
    ret = 0                     #O(1)
    for i in range(len(A)):     #O(n)
        ret += A[i] * B[i]      #O(1) * n
    return ret                  #O(1)

#Tsomma = O(n)
#Ssomma = O(1)


def concat(A,B):
    C = []                      #O(1)
    for i in range(len(A)):     #O(n)
        C.append(A[i])          #O(1) * n
    for i in range(len(B)):     #O(m)
        C.append(B[i])          #O(1) * m
    return C                    #O(1)

#Tsomma = O(n + m)
#Ssomma = O(n + m)


def merge(A,B):
    C = []                              #O(1)
    i = 0                               #O(1)
    j = 0                               #O(1)
    while(i < len(A) and j < len(B)):   #O(2 * min(n,m))
        if(A[i] < B[j]):                #O(1)
            C.append(A[i])              #O(1)
            i += 1                      #O(1)
        else:                               
            C.append(B[j])              #O(1)
            j += 1                      #O(1)
    while(i < len(A)):                  #O(n - min(n,m))
        C.append(A[i])                  #O(1)
        i += 1                          #O(1)
    while(j < len(B)):                  #O(m - min(n,m))
        C.append(B[j])                  #O(1)
        j += 1                          #O(1)
    return C                            #O(1)

#Tmerge = 2 * min(m,n) + max(m,n) - min(m,n) = max(m,n) + min(m,n) = m + n = O(m + n)
#Smerge = O(m + n)

