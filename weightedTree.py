

def tree(key, leftSon, rightSon, weight):
    return [[key, leftSon, rightSon], weight]

def leafNode(key, weight):
    return [[key, [],[]], weight]

def leftSon(node):
    return node[0][1]

def rightSon(node):
    return node[0][1]

def weight(node):
    return node[1]

def isEmpty(node):
    return node[1] == 0

def isLeaf(node):
    return isEmpty(leftSon(node)) and isEmpty(rightSon(node))