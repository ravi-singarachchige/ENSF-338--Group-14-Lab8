class GraphNode:
    def __init__(self, data):
        self.data = data
        self.parent = self
        self.rank = 0

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def addNode(self, data):
        node = GraphNode(data)
        self.nodes[data] = node
        return node

    def addEdge(self, n1, n2, weight=1):
        self.edges.append((n1, n2, weight))

    def find(self, node):
        if node != node.parent:
            node.parent = self.find(node.parent)
        return node.parent

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            if root1.rank > root2.rank:
                root2.parent = root1
            else:
                root1.parent = root2
                if root1.rank == root2.rank:
                    root2.rank += 1

    def mst(self):
        mst = Graph()
        self.edges.sort(key=lambda edge: edge[2])
        for edge in self.edges:
            node1, node2, weight = edge
            if mst.find(node1) != mst.find(node2):
                mst.union(node1, node2)
                mst.addEdge(node1, node2, weight)
        return mst