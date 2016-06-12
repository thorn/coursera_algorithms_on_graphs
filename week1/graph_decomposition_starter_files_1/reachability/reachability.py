#Uses python3

import sys

def reach(nodes, x, y):
    #write your code here
    neighbours = nodes[x]['neighbours']
    nodes[x]['visited'] = True
    if y in neighbours:
        return 1
    for node in neighbours:
        if not nodes[node]['visited']:
            result = reach(nodes, node, y)
            if result == 1: return result
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    nodes = list(({'visited': False, 'neighbours': neighbours} for neighbours in adj))
    print(reach(nodes, x, y))
