import math
import graphL

def createGraph(n):
    return graphL.createGraph(n)

def copyGraph(G):
    return graphL.copyGraph(G)

def printGraph(G):
    for i in range(len(G)):
        print(i, G[i])

def size(G):
    return len(G)

def nodes(G):
    return list(range(len(G)))

def isEdge(G, node1, node2):
    for edge in G[node1]:
        if edge[0] == node2:
            return True
    return False

def weight(G, node1, node2):
    for edge in G[node1]:
        if edge[0] == node2:
            return edge[1]
    return math.inf

def insertEdge(Graph, node1, node2, weight):
    if not isEdge(Graph, node1, node2):
        Graph[node1].append([node2, weight])
    else:
        for edge in Graph[node1]:
            if edge[0] == node2:
                edge[1] = weight

def deleteEdge(Graph, node1, node2):
    for edge in Graph[node1]:
        if edge[0] == node2:
            Graph.pop(edge)
            break

def neighbors(G, node):
    ret = 0
    for edge in G[node]:
        ret.append(edge[0])

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