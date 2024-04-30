import weightedGraphL as g
import math


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