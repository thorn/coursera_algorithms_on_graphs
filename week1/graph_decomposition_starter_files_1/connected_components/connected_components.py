#Uses python3

import sys


def explore(nodes, x):
    nodes[x]['visited'] = True
    for node in nodes[x]['neighbours']:
        if not nodes[node]['visited']:
            explore(nodes, node)

def number_of_components(adj):
    result = 0
    #write your code here
    nodes = list(({'visited': False, 'neighbours': neighbours} for neighbours in adj))
    for node in nodes:
        if not node['visited']:
            result += 1
            explore(nodes, nodes.index(node))
    return result

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
    print(number_of_components(adj))
