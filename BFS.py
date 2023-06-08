#Breadth first search è uno dei due tipi di visita di un grafo a partire dal nodo startingNode

import weightedGraphL as g          
#Import the file representing the kind of structure you are using, always as g


def breadthVisit(G, startingNode):
    edges = []
    reached = [False for i in range(len(G))]
    reached[startingNode] = True
    queue = [startingNode]
    while len(queue) != 0:
        interestingNode = queue.pop(0)
        adjacentNodes = g.neighbors(G, interestingNode)
        for node in adjacentNodes:
            if not reached[node[0]]:
                queue.append(node[0])
                reached[node[0]] = True
        edges.append(interestingNode)
    return edges

def edges(pred):
    E = []
    for i in range(len(pred)):
        if pred[i] != -1:
            E.append([pred[i], i])
    return E

def breadthVisit1(G, startingNode):
    pred = [-1 for i in range(len(G))]
    queue = [startingNode]
    while queue != []:
        nextNode = queue.pop(0)
        adj = g.neighbors(G, nextNode)
        for [y,w] in adj:
            if pred[y] == -1:
                queue.append(y)
                pred[y] = nextNode
    return edges(pred)
