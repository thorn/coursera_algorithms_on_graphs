#Uses python3

import sys

def has_cycle(node, nodes):
    if node['visited'] == 'now':
        return 1
    node['visited'] = 'now'
    for neighbour_index in node['neighbours']:
        if has_cycle(nodes[neighbour_index], nodes):
            return 1
    node['visited'] = False
    return 0

def acyclic(nodes):
    for node in nodes:
        if has_cycle(node, nodes):
            return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    nodes = list(({'visited': False, 'removed': False, 'neighbours': neighbours} for neighbours in adj))
    print(acyclic(nodes))
