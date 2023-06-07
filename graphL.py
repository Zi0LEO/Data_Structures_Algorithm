def createGraph(n):
    G = []
    for i in range(n):
        G.append([])
    return G

def copyGraph(G):
    C = []
    for i in range(len(G)):
        C.append([])
        for node in G[i]:
            C[i].append(node)
    return C

def graph2Matrix(G):
    n = len(G)
    M = []
    for i in range(n):
        M.append([])
        for j in range(n):
            M[i].append(0)
    for i in range(n):
        for j in G[i]:
            M[i][j] = 1
    return M

def printGraph(G):
    M = graph2Matrix(G)
    for i in range(len(M)):
        print(M[i])

def size(G):
    return len(G)

def nodes(G):
    return list(range(size(G)))

def isEdge(G, node1, node2):
    return node2 in G[node1]

def insertEdge(G, node1, node2):
    if not node2 in G[node1]:
        G[node1].append(node2)

def deleteEdge(G, node1, node2):
    if node2 in G[node1]:
        G[node1].remove(node2)

def neighbors(G, node):
    L = []
    for x in G[node]:
        L.append(x)
    return L