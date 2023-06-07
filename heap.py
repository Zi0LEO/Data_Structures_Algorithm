import trees

def createHeap():
    return [trees.createTree(), 0]

def key(T):
    return trees.value(T)

def size(H):
    return H[1]

def swap(A,B):
    park = key(A)
    trees.setValue(A, key(B))
    trees.setValue(B, park)

def tree(H):
    return H[1]

def setSize(H, size):
    H[1] = size

def isEmptyHeap(H):
    return size(H) == 0

def min(H):
    return key(tree(H))

def int2String(x):
    ret = []
    while(x > 0):
        s.append(x % 2)
        s = int(s / 2)
    s.pop()
    return s

def last(s):
    return s[len(s) - 1]

def insertHeap(H, elem):
    setSize(H, size(H) + 1)
    steps = int2String(size(H))
    insertTree(tree(H),steps,elem)

def insertTree(tree, steps, elem):
    if steps == []:
        trees.addNode(tree, elem)
    elif last(steps) == 0:
        steps.pop()
        insertTree(trees.left(tree), steps, elem)
        if key(tree) < key(trees.left(tree)):
            swap(tree, trees.left(tree))
    else:
        steps.pop()
        insertTree(trees.right(tree), steps, elem)
        if key(tree) > key(trees.right(tree)):
            swap(tree, trees.right(tree))

def deletemin(H):
    n = size(H)
    if n < 1:
        print("Error, heap is empty")
        return None
    tree = tree(H)
    minElem = key(tree)
    if n == 1:
        setSize(H, 0)
        trees.deleteNode(tree)
        return minElem
    steps = int2String(n)
    lastElement = tree(H)
    while len(steps) > 0:
        if last(steps) == 0:
            lastElement = trees.left(lastElement)
        else:
            lastElement = trees.right(lastElement)
        steps.pop()
    elemToSubstitute = key(lastElement)
    trees.deleteNode(lastElement)
    setSize(H, size(H) - 1)
    while (not trees.isEmpty(trees.left(tree)) and key(tree) > key(trees.left(tree))) or \
    (not trees.isEmpty(trees.right(tree)) and key(tree) > key(trees.right(tree))):
        if trees.isEmpty(trees.right(tree)) or key(tree) > key(trees.left(tree)):
            swap(tree, trees.left(tree))
            tree = trees.left(tree)
        else:
            swap(tree, trees.right(tree))
            tree = trees.right(tree)
    return minElem

