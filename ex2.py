import heapq
import time
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.nodes = set()
        self.adjacency_list = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.add(node)
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2, weight):
        self.adjacency_list[node1].append((node2, weight))
        self.adjacency_list[node2].append((node1, weight))

def slowSP(graph, source):
    distances = {node: float('inf') for node in graph.nodes}
    distances[source] = 0
    visited = set()

    while len(visited) < len(graph.nodes):
        min_node = None
        min_dist = float('inf')
        for node in graph.nodes:
            if node not in visited and distances[node] < min_dist:
                min_node = node
                min_dist = distances[node]

        if min_node is None:
            break

        visited.add(min_node)
        for neighbor, weight in graph.adjacency_list[min_node]:
            new_dist = distances[min_node] + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist

    return distances


def fastSP(graph, source):
    distances = {node: float('inf') for node in graph.nodes}
    distances[source] = 0
    pq = [(0, source)]

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        if curr_dist > distances[curr_node]:
            continue
        for neighbor, weight in graph.adjacency_list[curr_node]:
            new_dist = curr_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distances


def measure_performance(graph):
    slow_times = []
    fast_times = []

    for node in graph.nodes:
        start_time = time.time()
        slowSP(graph, node)
        slow_time = time.time() - start_time
        slow_times.append(slow_time)
        print(f"Node {node} - Slow Time: {slow_time}")

        start_time = time.time()
        fastSP(graph, node)
        fast_time = time.time() - start_time
        fast_times.append(fast_time)
        print(f"Node {node} - Fast Time: {fast_time}")

    return slow_times, fast_times

def plot_histogram(slow_times, fast_times):
    plt.hist(slow_times, bins=30, alpha=0.5, color='blue', label='Slow')
    plt.hist(fast_times, bins=30, alpha=0.5, color='brown', label='Fast')
    plt.xlabel('Execution Time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Execution Times Across All Nodes')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_edge(1, 2, 1)
    graph.add_edge(2, 3, 2)
    graph.add_edge(1, 3, 4)

    slow_times, fast_times = measure_performance(graph)
    avg_slow_time = sum(slow_times) / len(slow_times)
    max_slow_time = max(slow_times)
    min_slow_time = min(slow_times)

    avg_fast_time = sum(fast_times) / len(fast_times)
    max_fast_time = max(fast_times)
    min_fast_time = min(fast_times)

    print("Slow Algorithm:")
    print(f"Avg Time: {avg_slow_time}")
    print(f"Max Time: {max_slow_time}")
    print(f"Min Time: {min_slow_time}")

    print("Fast Algorithm:")
    print(f"Avg Time: {avg_fast_time}")
    print(f"Max Time: {max_fast_time}")
    print(f"Min Time: {min_fast_time}")

    plot_histogram(slow_times, fast_times)

# The histogram displays the distribution of execution times for both the slow and fast versions of Dijkstra's algorithm.
# Bars represent time ranges, with the height denoting frequency. Overlapping bars indicate instances where the fast algorithm's
# performance matches or lags behind the slow one. Since we only see one bar in the histogram, it is clear that the performances overlap 
# and there isn't any significant difference between the two peerformances.