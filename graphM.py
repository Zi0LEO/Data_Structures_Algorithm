def createGraph(n):
    return [[0] * n] * n

def copyGraph(G):
    n = len(G)
    C = []
    for i in range(n):
        C.append([])
        for j in range(n):
            C[i].append(G[i][j])
    return C

def printGraph(G):
    for i in range(len(G)):
        print(G[i])

def size(G):
    return len(G)

def nodes(G):
    return list(range(size(G)))

def isEdge(G, i, j):
    return G[i][j] == 1

def insertEdge(G, node1, node2):
    G[node1][node2] = 1

def deleteEdge(G, node1, node2):
    G[node1][node2] = 0

def neighbors(G, node):
    ret = []
    for i in range(len(G)):
        if G[node][i] == 1:
            ret.append(i)
    return ret

def outDegree(G, node):
    ret = 0
    for i in range(len(G)):
        ret += G[node][i]
    return ret

def inDegree(G, node):
    ret = 0
    for i in range(len(G)):
        ret += G[i][node]
    return ret
