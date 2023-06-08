import weightedGraphL as g
from BFS import edges

def depthVisit(G, startingNode):
    pred = [ - 1 for i in range(len(G))]
    reached = [False for i in range(len(G))]
    Stack = [startingNode]
    while Stack != []:
        interestingNode = Stack.pop()
        reached[interestingNode] = True
        adjacentNodes = g.neighbors(G, interestingNode)
        adjacentNodes.reverse()
        for node in adjacentNodes:
            if not reached[node[0]]:
                Stack.append(node[0])
                pred[node[0]] = interestingNode
    return edges(pred)

def depthVisitRec1(G, startingNode):
    pred = [-1 for i in range(len(G))]
    depthVisitRec2(G, startingNode, pred)
    return pred

def depthVisitRec2(G, node, edges):
    adj = g.neighbors(G,node)
    adj.reverse()
    for nodeToVisit in adj:
        if edges[nodeToVisit[0]] == -1:
            edges[nodeToVisit[0]] = node
            depthVisitRec2(G, nodeToVisit[0], edges)
    
