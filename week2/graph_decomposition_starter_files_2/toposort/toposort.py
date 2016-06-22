#Uses python3
import sys

def dfs(nodes, order, node):
    node["visited"] = True
    for neighbour_index in node["neighbours"]:
        neighbour = nodes[neighbour_index]
        if not neighbour["visited"]:
            dfs(nodes, order, neighbour)

    order.append(node["index"])

def toposort(adj):
    order = []
    #write your code here
    nodes = list(({ "visited": False, "neighbours": neighbours, "index": index } for index, neighbours in enumerate(adj)))
    for node in nodes:
        if not node["visited"]:
            dfs(nodes, order, node)

    return reversed(order)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

