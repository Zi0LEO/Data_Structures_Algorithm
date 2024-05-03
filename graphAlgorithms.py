import weightedGraphL as g
import math
import heap 
import weightedTree as wTree

def dijkstra(graph, start):
    size = g.size(graph)
    visited = [False for i in range(size)]
    pred = [-1 for i in range(size)]
    dist = [math.inf for i in range(size)]
    dist[start] = 0
    for i in range(size):
        next = closestNode(dist, visited)
        visited[next] = True
        adjacentNodes = g.neighbors(graph, next)
        for [node, weight] in adjacentNodes:
            if not visited[node] and dist[next] + weight < dist[node]:
                dist[node] = dist[next] + weight
                pred[node] = next
    return pred, dist

def closestNode(dist, visited):
    node = 0
    currentMinDistance = math.inf
    for i in range(len(visited)):
        if not visited[i] and dist[i] < currentMinDistance:
            node = i
            currentMinDistance = dist[i]
    return node

def copyList(list):
    copy = []
    for i in range(len(list) - 1):
        copy.append(list[i])
    return copy;


def codeGeneration(tree, retList, partialCode):
    if wTree.isLeaf(tree):
        D = copyList(partialCode)
        retList.append([wTree.key(tree), D])
    else:
        partialCode.append(0)
        codeGeneration(wTree.leftSon(tree), retList, partialCode)
        partialCode.pop()
        partialCode.append(1)
        codeGeneration(wTree.rightSon(tree), retList, partialCode)



def huffman(L):
    Q = heap.createHeap()
    n = len(L)
    for(char, frequency) in L:
        T = wTree.leafNode(char, frequency)
        heap.insertHeap(Q, T)
    for i in range(n - 1):
        A = heap.deleteMin(Q)
        B = heap.deleteMin(Q)
        C = wTree.tree('_',A,B,wTree.weight(A) + wTree.weight(B))
        heap.insertHeap

