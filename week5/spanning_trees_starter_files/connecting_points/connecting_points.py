#Uses python3
import sys
import math

def MakeSet(x):
     x.parent = x
     x.rank   = 0

def Union(x, y):
     xRoot = Find(x)
     yRoot = Find(y)
     if xRoot.rank > yRoot.rank:
         yRoot.parent = xRoot
     elif xRoot.rank < yRoot.rank:
         xRoot.parent = yRoot
     elif xRoot != yRoot:
         yRoot.parent = xRoot
         xRoot.rank = xRoot.rank + 1

def Find(x):
     if x.parent == x:
        return x
     else:
        x.parent = Find(x.parent)
        return x.parent

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = False
        self.rank = 0

    def __str__(self):
        return "[%d, %d] parent: %d, rank: %d" % (self.x, self.y, (self.parent and True), self.rank)

class Edge:
    def __init__(self, x_node, y_node):
        self.x_node = x_node
        self.y_node = y_node
        self.distance = self.calculate_distance()

    def __str__(self):
        return "[%d,%d] - [%d,%d]: %f" % (self.x_node.x, self.x_node.y, self.y_node.x, self.y_node.y, self.distance)

    def calculate_distance(self):
        return math.sqrt(math.pow((self.x_node.x - self.y_node.x), 2) + math.pow((self.x_node.y - self.y_node.y ), 2))

def construct_edges(nodes):
    edges = []
    for x_node in nodes:
        for y_node in nodes:
            if x_node != y_node:
                edges.append(Edge(x_node, y_node))

    return sorted(edges, key=lambda edge: edge.distance)

def minimum_distance(x, y):
    result = 0.
    #write your code here
    result_edges = []
    nodes = [Node(x_coord, y[index]) for index, x_coord in enumerate(x)]
    [MakeSet(node) for node in nodes]

    edges = construct_edges(nodes)
    for edge in edges:
        if Find(edge.x_node) != Find(edge.y_node):
            result_edges.append(edge)
            Union(edge.x_node, edge.y_node)

    for edge in result_edges:
        result += edge.distance

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
