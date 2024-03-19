class GraphNode:
    def __init__(self, data):
        self.data = data

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def addNode(self, data):
        node = GraphNode(data)
        self.nodes[data] = node
        return node

    def removeNode(self, node):
        del self.nodes[node.data]
        for n, edges in self.edges.items():
            if node.data in edges:
                del edges[node.data]

    def addEdge(self, n1, n2, weight=1):
        if n1.data not in self.edges:
            self.edges[n1.data] = {}
        if n2.data not in self.edges:
            self.edges[n2.data] = {}
        self.edges[n1.data][n2.data] = weight
        self.edges[n2.data][n1.data] = weight

    def removeEdge(self, n1, n2):
        del self.edges[n1.data][n2.data]
        del self.edges[n2.data][n1.data]

    def importFromFile(self, file):
        try:
            with open(file, 'r') as f:
                lines = f.readlines()
            if not lines[0].startswith('strict graph'):
                return None
            self.nodes = {}
            self.edges = {}
            for line in lines[1:-1]:
                line = line.strip()
                if '[' in line:
                    n1, rest = line.split(' -- ')
                    n2, weight = rest.split(' [weight=')
                    weight = int(weight[:-2])
                else:
                    n1, n2 = line.split(' -- ')
                    weight = 1
                self.addNode(n1)
                self.addNode(n2)
                self.addEdge(self.nodes[n1], self.nodes[n2], weight)
        except Exception as e:
            return None