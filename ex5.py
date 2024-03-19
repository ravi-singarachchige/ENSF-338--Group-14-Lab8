#Question 1

#Topological sorting can be implemented using Depth-First Search (DFS) algorithm. 
#The reason is that DFS visits all nodes of a graph in a depthward motion first, which is useful to detect the dependencies between nodes. 
#In a Directed Acyclic Graph (DAG), topological sorting can be viewed as ordering the nodes in such a way that all directed edges go from left to right.

#Question 2 and 3

class Graph(Graph):
    def isdag(self):
        visited = set()
        recursion_stack = set()

        for node in self.nodes.values():
            if node.data not in visited:
                if self._has_cycle(node, visited, recursion_stack):
                    return False
        return True

    def _has_cycle(self, node, visited, recursion_stack):
        visited.add(node.data)
        recursion_stack.add(node.data)

        for neighbor in self.edges[node.data]:
            if neighbor not in visited:
                if self._has_cycle(self.nodes[neighbor], visited, recursion_stack):
                    return True
            elif neighbor in recursion_stack:
                return True

        recursion_stack.remove(node.data)
        return False

    def toposort(self):
        if not self.isdag():
            return None

        visited = set()
        stack = []

        for node in self.nodes.values():
            if node.data not in visited:
                self._toposort_visit(node, visited, stack)

        return stack[::-1]

    def _toposort_visit(self, node, visited, stack):
        visited.add(node.data)

        for neighbor in self.edges[node.data]:
            if neighbor not in visited:
                self._toposort_visit(self.nodes[neighbor], visited, stack)

        stack.append(node.data)