import heapq
import itertools


# Step 1: Construct the Graph with Weighted Edges
class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = []

    def add_edge(self, from_node, to_node, weight):
        self.add_node(from_node)
        self.add_node(to_node)
        self.nodes[from_node].append((to_node, weight))


# Example graph construction
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 2)
graph.add_edge('B', 'D', 3)
graph.add_edge('B', 'E', 1)
graph.add_edge('C', 'F', 4)


# Step 2: Define WHS Search Algorithm

def whs_search(graph, start, target):
    priority_queue = []
    counter = itertools.count()  # Unique sequence count
    heapq.heappush(priority_queue, (0, next(counter), start, []))  # (cumulative_weight, counter, current_node, path)
    visited = set()

    while priority_queue:
        cumulative_weight, _, current_node, path = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)
        new_path = path + [current_node]

        if current_node == target:
            return new_path, cumulative_weight

        for neighbor, weight in graph.nodes.get(current_node, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cumulative_weight + weight, next(counter), neighbor, new_path))

    return None, None


# Example usage
start_node = 'A'
target_value = input("Please Enter the Target Node: ").upper()
path, total_weight = whs_search(graph, start_node, target_value)

if path:
    print(f"Path found to node {target_value}: {path} with total weight {total_weight}")
else:
    print(f"No path found to node {target_value}.")
