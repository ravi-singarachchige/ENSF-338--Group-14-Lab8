#Question 1 and 2
import numpy as np

class Graph2:
    def __init__(self):
        self.nodes = {}
        self.matrix = np.zeros((0, 0))

    def addNode(self, data):
        if data not in self.nodes:
            self.nodes[data] = len(self.nodes)
            self.matrix = np.pad(self.matrix, ((0, 1), (0, 1)))

    def removeNode(self, node):
        del self.nodes[node.data]
        self.matrix = np.delete(self.matrix, self.nodes[node.data], axis=0)
        self.matrix = np.delete(self.matrix, self.nodes[node.data], axis=1)

    def addEdge(self, n1, n2, weight=1):
        self.matrix[self.nodes[n1.data], self.nodes[n2.data]] = weight
        self.matrix[self.nodes[n2.data], self.nodes[n1.data]] = weight

    def removeEdge(self, n1, n2):
        self.matrix[self.nodes[n1.data], self.nodes[n2.data]] = 0
        self.matrix[self.nodes[n2.data], self.nodes[n1.data]] = 0

    def dfs(self):
        visited = set()
        order = []

        def dfs_visit(node):
            visited.add(node)
            order.append(node)
            for i, weight in enumerate(self.matrix[self.nodes[node]]):
                if weight > 0 and list(self.nodes.keys())[i] not in visited:
                    dfs_visit(list(self.nodes.keys())[i])

        dfs_visit(list(self.nodes.keys())[0])
        return order

class Graph(Graph):
    def dfs(self):
        visited = set()
        order = []

        def dfs_visit(node):
            visited.add(node.data)
            order.append(node.data)
            for neighbor, weight in self.edges[node.data].items():
                if weight > 0 and neighbor not in visited:
                    dfs_visit(self.nodes[neighbor])

        dfs_visit(list(self.nodes.values())[0])
        return order

#Question 3    
import timeit

g1 = Graph()
g1.importFromFile('random.dot')
g2 = Graph2()
g2.importFromFile('random.dot')

times1 = timeit.repeat(lambda: g1.dfs(), repeat=10, number=1)
times2 = timeit.repeat(lambda: g2.dfs(), repeat=10, number=1)

print('Graph dfs() min: {}, max: {}, avg: {}'.format(min(times1), max(times1), sum(times1)/len(times1)))
print('Graph2 dfs() min: {}, max: {}, avg: {}'.format(min(times2), max(times2), sum(times2)/len(times2)))