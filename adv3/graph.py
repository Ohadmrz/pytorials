from typing import Any


class Graph:

    def __init__(self):
        self._nodes = []
        self._edges: dict[Any, list] = {}

    def add_node(self, node):
        self._nodes.append(node)
        self._edges[node] = []

    def add_edge(self, from_node, to_node):

        if from_node not in self._nodes or to_node not in self._nodes:
            raise Exception("Node does not exist in the graph")

        self._edges[from_node].append(to_node)

    def is_reachable(self, from_node, to_node):

        # Create an empty set to store visited nodes
        visited = set()

        # Create a queue for BFS and add from_node to it
        queue = [from_node]

        # Mark the from_node as visited and enqueue it
        visited.add(from_node)

        while queue:

            # Dequeue a vertex from queue
            curr_node = queue.pop(0)

            # If this adjacent node is the destination node,
            # then return true
            if curr_node == to_node:
                return True

            #  Else, continue to do BFS
            for node in self._edges[curr_node]:
                if node not in visited:
                    queue.append(node)
                    visited.add(node)

        # If BFS is complete without visited d
        return False

    def dfs(self, from_node, to_node) -> bool:
        return self._dfs_rec(from_node, to_node, set())

    def _dfs_rec(self, from_node, to_node, visited) -> bool:

        if from_node == to_node:
            return True

        visited.add(from_node)
        for node in self._edges[from_node]:
            if node not in visited:
                if self._dfs_rec(node, to_node, visited):
                    return True
        return False


if __name__ == '__main__':

    graph = Graph()
    for city in ('Brussels', 'Kyoto', 'Amsterdam',
                 'Tokyo', 'Tel Aviv', 'Paris', 'London', 'Hong Kong'):
        graph.add_node(city)

    graph.add_edge('Brussels', 'Tel Aviv')
    graph.add_edge('Brussels', 'Tokyo')

    graph.add_edge('Tokyo', 'Kyoto')
    graph.add_edge('Tokyo', 'Hong Kong')

    graph.add_edge('Tel Aviv', 'Paris')

    graph.add_edge('Hong Kong', 'Tel Aviv')

    graph.add_edge('Paris', 'Amsterdam')
    graph.add_edge('Paris', 'London')

    # print(f"Path from Brussels to Amsterdam: {graph.is_reachable('Brussels', 'Amsterdam')}")
    # print(f"Path from Tokyo to Brussels: {graph.is_reachable('Tokyo', 'Brussels')}")

    print(f"Path from Brussels to Amsterdam: {graph.dfs('Brussels', 'Amsterdam')}")
    print(f"Path from Tokyo to Brussels: {graph.dfs('Tokyo', 'Brussels')}")

