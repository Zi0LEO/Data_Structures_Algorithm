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

print("BREADTH VISIT: ")
G = g.createGraph(5)
e = [[1,3,1], [3,1,1], [1,2,1], [2,1,1], [1,4,1], [4,1,1], [3,4,1], [3,4,1], [2,4,1], [4,2,1], [2,0,1], [0,2,1], [4,0,1], [0,4,1]]
for [x,y,w] in e:
    g.insertEdge(G, x,y,w)
g.printGraph(G)
print()
print(breadthVisit1(G,3))
print()
print()