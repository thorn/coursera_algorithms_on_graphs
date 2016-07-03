#Uses python3

import sys

def relax(nodes, node):
    information_changed = False
    for index, neighbour_index in enumerate(node["neighbours"]):
        neighbour = nodes[neighbour_index]
        extended_distance = node["distance"] + node["cost"][index]
        if neighbour["distance"] > extended_distance:
            neighbour["distance"] = extended_distance
            information_changed = True
    return information_changed

def negative_cycle(adj, cost):
    #write your code here
    nodes = list({"neighbours": neighbours, "cost": cost[index], "distance": float("inf"), "index": index} for index, neighbours in enumerate(adj))
    new_source_node = {"neighbours": list(i for i in range(len(nodes))), "cost": list(0 for i in range(len(nodes))), "distance": 0, "index": len(nodes)}
    nodes.append(new_source_node)
    for i in range(len(nodes) - 1):
        for node in nodes:
            relax(nodes, node)

    for node in nodes:
        if relax(nodes, node) == True:
            return 1

    return 0


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
    print(negative_cycle(adj, cost))
