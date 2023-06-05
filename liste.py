def createList():
    return []

def insertTail(L, x):
    if L == []:
        L.append(x)
        L.append([])
    else:
        insertTail(L[1], x)

def insertHead(L,x):
    if L == []:
        L.append(x)
        L.append([])
    else:
        [key, next] = [L[0], L[1]]
        L[0] = x
        L[1] = [key, next]

def listToArray(L, A):
    if L == []:
        return
    A.append(L[0])
    listToArray(L[1], A)

L1 = createList()
insertHead(L1, 5)
insertHead(L1, 7)
insertHead(L1, 4)
insertHead(L1, 2)
print(L1)
A1 = []
listToArray(L1, A1)
print(A1)