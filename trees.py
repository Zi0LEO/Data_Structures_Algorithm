def createTree():
    return[]

def isEmpty(A):
    return A == []

def value(A):
    return A[0]

def left(A):
    return A[1]

def right(A):
    return A[2]

def setValue(A, x):
    A[0] = x

def setLeft(A, p):
    A[1] = p

def setRight(A, p):
    A[2] = p

def addNode(A, x):
    A.append(x)
    A.append([])
    A.append([])

def deleteNode(A):
    A.pop()
    A.pop()
    A.pop()

def copyNode(A,B):
    A[0] = B[0]
    A[1] = B[1]
    A[2] = B[2]

def findMax(A):
    if isEmpty(right(A)):
        return value(A)
    return findMax(right(A))

def findMin(A):
    if isEmpty(left(A)):
        return value(A)
    return findMin(left(A))

def depth(A):
    if isEmpty(A):
        return 0
    return max(depth(right(A)), depth(left(A))) + 1

def balance(A):
    if isEmpty(A):
        return 0
    return depth(left(A)) - depth(right(A))

def rightRotate(A):
    park  = A
    A = left(A)
    setLeft(park, right(A))
    setRight(A, park)
    return A

def leftRotate(A):
    park = A
    A = right(A)
    setRight(park, left(A))
    setLeft(A, park)
    return A

def rotate(A):
    if not isEmpty(A):
        if balance(A) == 2:
            if balance(left(A)) >= 0:
                A = rightRotate(A)
            else:
                setLeft(A, leftRotate(left(A)))
                A = rightRotate(A)
        if balance(A) == -2:
            if(balance(right(A))) >= 0:
                A = leftRotate(A)
            else:
                setRight(A, rightRotate(right(A)))
                A = leftRotate(A)
    return A

def search(A, x):
    if isEmpty(A):
        return False
    if value(A) == x:
        return True
    if x > value(A):
        return search(right(A), x)
    return search(left(A), x)

def insert(A, x):
    if isEmpty(A):
        addNode(A, x)
    elif value(A) == x:
        print("Value is already in the tree")
    elif x > value(A):
        insert(right(A), x)
    else:
        insert(left(A), x)
    return rotate(A)

def delete(A, x):
    if isEmpty(A):
        return A
    if x == value(A):
        if isEmpty(left(A)) and isEmpty(right(A)):
            deleteNode(A)
        elif isEmpty(left(A)) and not isEmpty(right(A)):
            copyNode(A, right(A))
        elif isEmpty(right(A)) and not isEmpty(left(A)):
            copyNode(A, left(A))
        else:
            currentMax = findMax(left(A))
            setValue(A,y)
            setLeft(left(A), delete(left(A), y))
    elif x < value(A):
        setLeft(A,delete(left(A), x))
    else:
        setLeft(A, delete(right(A), x))
    return rotate(A)
