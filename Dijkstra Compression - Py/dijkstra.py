from PriorityQueueHeap import *
import math

INF = math.inf

test= [ [], 
        [(2, 20), (6, 50)],
        [(1, 20), (3, 70), (6, 30), (5, 10)],
        [(2,70), (5, 40), (4, 90)],
        [(5, 60), (3, 90)],
        [(4, 60), (3, 40), (2, 10), (6, 80)],
        [(5, 80), (1, 50), (2, 30)] ]


def dijkstra(start, map):
    """ Takes a start vertex number, end vertex number, and a map
    in adjacency list form and returns the length of the shortest path
    from start to end. """
    Q = PriorityQueueHeap()
    n = len(map)
    Distance = [None] * n  # Array of distances from start
    #student code
    Distance = [INF] * n
    Distance[start] = 0
    vertex = Item(0, start)
    Q.insert(vertex)
    while Q.elements != 0:
        minver = Q.deleteMin()
        leftind = 2* Q.index[minver]
        rightind = 2* Q.index[minver] + 1
        
