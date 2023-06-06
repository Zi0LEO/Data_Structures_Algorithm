import trees

def createHeap():
    return [trees.createTree(), 0]

def size(H):
    return H[1]

def tree(H):
    return H[1]

def setSize(H, size):
    H[1] = size

def isEmptyHeap(H):
    return size(H) == 0

def min(H):
    return trees.value(tree(H))
