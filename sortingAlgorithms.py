def insertionSort(A):
    for i in range(1, len(A)):              #O(n)
        min = A[i]                          #O(1) * n - 1
        j = i                               #O(1) * n - 1
        while j > 0 and A[j - 1] > min:     #*
            A[j] = A[j - 1]                 #O(1)
            j = j - 1                       #O(1)
        A[j] = min                          #O(1)

#*Questo controllo dovrà essere svolto n volte nel caso migliore, cioè se la lista è già ordinata, 
#oppure può essere svolto i volte ad ogni iterazione nel caso peggiore, cioè se la lista è ordinata in ordine decrescente,
#nel caso peggiore quindi, contando che i va da 1 a n - 1, la complessità sarà la sommatoria da 1 a n - 1 di
#i, cioè 1+2+3+...+(n-1), questa sommatoria si può approssimare a (n^2)/2

#T(n)best = n * T2 + (n-1) * (T3 + T4 + T5 + T6 + T7 + T8) = O(n)
#T(n)worst = n * T2 + (n-1) * (T3 + T4 + T8) * ((n^2)* 2) * (T6 + T7) = O(n^2)

# O(n) <= TinsertionSort <= O(n^2)

def selectionSort(A):
    for i in range(len(A) - 1):         #O(n)
        minp = i
        for j in range(i + 1, len(A)):  #*
            if A[j] < A[i]:             #O(1)
                minp = j
            A[i], A[minp] = A[minp], A[i] #O(1)

#*Questo controllo andrà svolto sempre per intero, la sua complessità perciò sarà la sommatoria di k che va da
#1 a n - 1, dove n è la lunghzza della lista.
#T(n) = O(n^2)



list = [6,3,8,2,5,9,1,4]
print(list)
selectionSort(list)
print(list)