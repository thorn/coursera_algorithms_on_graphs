#Uses python3

import sys
import queue

def find_min(nodes):
    left_nodes = (node for node in nodes if node["visited"] is False)
    minimum = min(left_nodes, key=lambda node: node["distance"], default=False)
    return minimum

def distance(adj, cost, s, t):
    #write your code here
    nodes = list({"visited": False, "neighbours": neighbours, "cost": cost[index], "distance": 10000000, "prev": False, "index": index} for index, neighbours in enumerate(adj))
    nodes[s]["distance"] = 0
    for min_node in iter(lambda: find_min(nodes), False):
        min_node["visited"] = True
        for index, neighbour_index in enumerate(min_node["neighbours"]):
            neighbour = nodes[neighbour_index]
            extended_distance = min_node["distance"] + min_node["cost"][index]
            if neighbour["distance"] > extended_distance:
                neighbour["distance"] = extended_distance
                min_node["prev"] = min_node["index"]
        if min_node["index"] == t:
            if min_node["distance"] == 10000000:
                return -1
            else:
                return min_node["distance"]

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
