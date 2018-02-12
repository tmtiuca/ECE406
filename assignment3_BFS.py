#!/usr/bin/env python3
"""
ECE406
Python file for assignment 3, Exercise 5

we will use the queue module to implement a FIFO queue.
- you can create a queue with Q = queue.queue(max_size)
- you can inject v onto the queue with Q.put(v)
- you can eject from the queue with Q.get()
"""
import queue

def shortest_path(u, v, adj):
    q = queue.Queue()
    visited = [False] * len(adj)
    dist = [len(adj)] * len(adj)

    dist[u] = 0

    q.put(u)

    while not q.empty():
        current = q.get()

        visited[current] = True

        if current is v:
            return dist[v]

        for child in adj[current]:
            if dist[current] + 1 < dist[child]:
                dist[child] = dist[current] + 1

            if not visited[child]:
                q.put(child)

def all_shortest_paths(u, adj):
    q = queue.Queue()
    visited = [False] * len(adj)
    dist = [len(adj)] * len(adj)

    dist[u] = 0

    q.put(u)

    while not q.empty():
        current = q.get()

        visited[current] = True

        for child in adj[current]:
            if dist[current] + 1 < dist[child]:
                dist[child] = dist[current] + 1

            if not visited[child]:
                q.put(child)

    return dist

def shortest_v_paths(adj, vertex_s):
    """
    Input:  1) A directed graph represented as an adjacency list adj:
                adj[1] is a list containing the neighbors of vertex 1
                (by default, vertices are numbered from 0 to |V| - 1)
            2) a vertex_s in 0,...,|V|-1

    Output: a matrix of distances, where M[i,j] gives the length of the shortest
            path from vertex i to vertex j passing through vertex_s
    """

    paths_to_v = [0 for x in adj]
    paths_from_v = [0 for x in adj]

    for vertex in range(0, len(adj)):
        if vertex is vertex_s:
            paths_from_v = all_shortest_paths(vertex, adj)

        paths_to_v[vertex] = shortest_path(vertex, vertex_s, adj)

    dist = []

    for i in range(0, len(adj)):
        dist.append([0] * len(adj))

    for u in range(0, len(adj)):
        for v in range(0, len(adj)):
            dist[u][v] = paths_to_v[u] + paths_from_v[v]

    return dist

def main():
    """
    A simple test case for your algorithm with four vertices 0,1,2,3
    """
    adj = [[1],
           [2, 3],
           [1, 3],
           [0]]

    # test case:
    mat = shortest_v_paths(adj, 3)
    print('\nTest Case:')
    for row in mat:
        print(row)

if __name__ == '__main__':
    main()
