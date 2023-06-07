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