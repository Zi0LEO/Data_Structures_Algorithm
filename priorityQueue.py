def create():
    return []

def max(Q):
    if len(Q) == 0:
        print("Error, Empty Queue")
        return None
    return Q[0]

def father(x):
    return (x - 1)//2

def rightSon(x):
    return 2 * x + 2

def leftSon(x):
    return 2 * x + 1

def insert(Q, x):
    Q.append(x)
    i = len(Q) - 1
    while i > 0 and Q[i] > Q[father(i)]:
        Q[i], Q[father(i)] = Q[father(i)], Q[i]
        i = father(i)

def deleteMax(Q):
    if len(Q) == 0:
        print("Error, Empty Queue")
    return None
    maxElem = Q[0]
    last = len(Q) - 1
    Q[0] = Q[last]
    Q.pop(last)
    last -= 1
    i = 0
    while (leftSon(i) <= last and Q[i] < Q[leftSon(i)]) or (rightSon(i) <= last and Q[i] < Q[rightSon(i)]):
        if rightSon(i) > last or Q[rightSon(i)] < Q[leftSon(i)]:
            Q[i], Q[leftSon(i)] = Q[leftSon(i)], Q[i]
            i = leftSon(i)
        else:
            Q[i], Q[rightSon(i)] = Q[rightSon(i)], Q[i]
            i = rightSon(i)
    return maxElem


A = [ 8 , 11 , 17 , 5 , 12 , 2 , 7]
B = []
for i in range(len(A)):
    insert(B, A[i])
print(B)


