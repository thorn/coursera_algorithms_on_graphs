#Uses python3

import sys
import queue

def bipartite(adj):
    #write your code here
    nodes = list(({ "distance": -1, "neighbours": neighbours, "color": False } for neighbours in adj))
    start_node = nodes[0]
    start_node["distance"] = 0
    start_node["color"] = "white"

    worker = queue.Queue()
    worker.put(start_node)

    while not worker.empty():
        node = worker.get()
        for neighbour_index in node["neighbours"]:
            neighbour = nodes[neighbour_index]
            if neighbour["distance"] == -1:
                worker.put(neighbour)
                neighbour["distance"] = node["distance"] + 1
                if node["color"] == "white":
                    neighbour["color"] = "black"
                elif node["color"] == "black":
                    neighbour["color"] = "white"
            else:
                if neighbour["color"] == node["color"] and neighbour["distance"] == node["distance"]:
                    return 0

    return 1

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
    print(bipartite(adj))
