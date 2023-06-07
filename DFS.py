import weightedGraphL as g
import BFS

def depthVisit(G, startingNode):
    pred = [ - 1 for i in range(len(G))]
    reached = [False for i in range(len(G))]
    Stack = [startingNode]
    while Stack != []:
        interestingNode = Stack.pop()
        reached[interestingNode] = True
        adjacentNodes = g.neighbors(G, interestingNode)
        adjacentNodes.reverse()ù
        for node in adjacentNodes:
            if not reached[node[0]]:
                Stack.append(node[0])
                pred[node[0]] = interestingNode
    return BFS.edges(pred)

print("DEPTH VISIT: ")
G = g.createGraph(5)
e = [[1,3,1], [3,1,1], [1,2,1], [2,1,1], [1,4,1], [4,1,1], [3,4,1], [3,4,1], [2,4,1], [4,2,1], [2,0,1], [0,2,1], [4,0,1], [0,4,1]]
for [x,y,w] in e:
    g.insertEdge(G, x,y,w)
g.printGraph(G)
print()
print(depthVisit(G,3))
print()
print()