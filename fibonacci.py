def fib(n):
    if n == 0 or n == 1:                    #O(1)
        return n                            #O(1)
    else:
        return fib(n - 1) + fib(n - 2)      #O(1) * (Tfib(n-1) + Tfib(n-2))
    
#                                    fib(n)  ---> C == (2^0)C
#                                     / \
#                                    /   \
#                            fib(n-1)     fib(n-2) ---> 2C == (2^1)C
#                           / \                 / \
#                          /   \               /   \
#                   fib(n-2)    fib(n-3) fib(n-3)   fib(n-4) ---> 4C == (2^2)C
#                  / \            / \    / \                 / \
#
# Il ramo che impiegherà più tempo ad arrivare al caso base sarà sempre il ramo più a sinistra dell'albero,
# al contrario, il più veloce sarà sempre quello più a destra. Notando in che modo l'albero cresce, possiamo
# dire che l'upper bound della funzione, nel caso del ramo sinostro sarà o(2^n)
#
#Tfib(n) = {O(1) se n == 0 o  n == 1, o(2^n) altrimenti}
#Sfib(n) = {O(1 ) se n == 0 o n == 1, O(n) altrimenti

def fib1(n):
    F = [0,1]                               #O(1)
    for i in range(2, n+1):                 #O(n)
        F.append(F[i - 1] + F[i - 2])       #O(1)
    return F[n]                             #O(1)

#Tfib1(n) = O(n)
#Sfib1(n) = O(n)


def fib2(n):
    if n == 0:
        return 0
    F = [0,1]
    for i in range(2, n+1):                 #O(n)
        F[0], F[1] = F[1], F[0] + F[1]       #O(1)
    return F[1]                             #O(1)

#Tfib2(n) = O(n)
#Sfib2(n) = O(1)


def fib3(n):
    if n == 0:
        return 0
    F0 = 0
    F1 = 1
    for i in range(2, n+1):
        F0, F1 = F1, F0 + F1
    return F1

#Tfib3(n) = O(n)
#Sfib3(n) = O(n)


import time
n = 40
t0 = time.time()
f0 = fib(n)
t1 = time.time()
f1 = fib1(n)
t2 = time.time()
f2 = fib2(n)
t3 = time. time()
f3 = fib3(n)
t4 = time.time()
print("Risultato e Tempo versione iterativa con lista: ", f1, t2 - t1)
print("Risultato e tempo versione iterativa senza lista: ", f2, t3 - t2)
print("Risultato e tempo versione ricorsiva lineare: ", f3, t4 - t3)
print("Risultato e tempo versione ricorsiva non lineare: ", f0 , t1 - t0)
