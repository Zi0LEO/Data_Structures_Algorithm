def printMatrix(M):
    for i in range(len(M)):
        print(M[i])

def somma(A,B):
    C = []                                  #O(1)
    for i in range(len(A)):                 #O(n)
        C.append([])                        #O(1) * n
        for j in range(len(A[0])):          #O(m) * n
            C[i].append(A[i][j] + B[i][j])  #O(1) * n * m
    return C                                #O(1)

#Tsomma = O(n * m)
#Ssomma = O(n * m)


def prod(A,B): 
    C = []                                      #O(1)
    for i in range(len(A)):                     #O(n)
        C.append([])                            #O(1) * n
        for j in range(len(B[0])):              #O(m) * n
            C[i].append(0)                      #O(1) * m * n
            for k in range(len(B)):             #O(p) * m * n
                C[i][j] +=  A[i][k] * B[k][j]   #O(1) * p * m * n
    return C                                    #O(1)

#Tprod = O(m * n * p)
#Sprod = O(m * n)