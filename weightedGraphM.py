import math
import graphM

def createGraph(n):
    return [[math.inf for x in range(n)] for y in range(n)]

def copyGraph(G):
    return graphM.copyGraph(G)

def printGraph(G):
    return graphM.printGraph(G)

def size(G):
    return len(G)

def nodes(G):
    return list(range(len(G)))

def isEdge(Graph, node1, node2):
    return Graph[node1][node2] != math.inf

def weight(Graph, node1, node2):
    return Graph[node1][node2]

def insertEdge(Graph, node1, node2, weight):
    Graph[node1][node2] = weight

def deleteEdge(Graph, node1, node2):
    Graph[node1][node2] = math.inf

def outDegree(Graph, node):
    ret = 0
    for i in range(len(Graph)):
        if Graph[node][i] != math.inf:
            ret += 1
    return ret

def inDegree(Graph, node):
    ret = 0
    for i in range(len(Graph)):
        if Graph[i][node] != math.inf:
            ret += 1
    return ret

def neighbors(Graph, node):
    ret = []
    for i in nodes(Graph):
        if isEdge(Graph, node, i):
            ret.append(i)
    return ret


G = createGraph(6)
print("Grafo con 6 nodi ma nessun arco")
printGraph(G)
E = [ [ 0 , 1 , 2 ] , [ 0 , 5 , 9 ] , [ 1 , 2 , 6 ] , [ 1 , 3 , 8 ] , [ 1 , 5 , 5 ] , [ 2 , 3 , 1 ] , [ 4 , 2 , 7 ] ,
[ 4 , 3 , 3 ] , [ 5 , 4 , 3 ] ]
for [x,y,w] in E:
    insertEdge(G, x,y,w)
print()
print("Grafo con 6 nodi e 9 archi pesati")
printGraph(G)