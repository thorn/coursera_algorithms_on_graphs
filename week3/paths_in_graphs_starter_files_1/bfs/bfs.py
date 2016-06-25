#Uses python3

import sys
import queue

def distance(adj, s, t):
    #write your code here
    nodes = list(({ "distance": -1, "neighbours": neighbours } for neighbours in adj))
    start_node = nodes[s]
    start_node["distance"] = 0

    worker = queue.Queue()
    worker.put(start_node)

    while not worker.empty():
        node = worker.get()
        for neighbour_index in node["neighbours"]:
            neighbour = nodes[neighbour_index]
            if neighbour["distance"] == -1:
                worker.put(neighbour)
                neighbour["distance"] = node["distance"] + 1
            if neighbour_index == t:
                return neighbour["distance"]
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
