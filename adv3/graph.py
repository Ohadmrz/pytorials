import pprint
from typing import Any


class Graph:

    def __init__(self):
        self._edges: dict[Any, list] = {}

        # {'Brussels': ['Paris'],
        #
        # }

    def _validate_nodes_exist(self, *args):
        for node in args:
            if node not in self._edges.keys():
                raise Exception("Node does not exist in the graph")

    def add_node(self, node):
        self._edges[node] = []

    def add_edge(self, from_node, to_node):

        self._validate_nodes_exist(from_node, to_node)
        self._edges[from_node].append(to_node)

    def is_adjacent(self, node1, node2):
        self._validate_nodes_exist(node1, node2)
        if node2 in self._edges[node1]:
            return -1
        elif node1 in self._edges[node2]:
            return 1
        else:
            return 0

    def bfs(self, from_node, to_node):

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

    def dfs_with_depth(self, from_node, to_node) -> tuple[bool, int] | tuple[bool, None]:
        return self._dfs_rec_with_depth(from_node, to_node, set(), 0)

    def _dfs_rec_with_depth(self, from_node, to_node, visited, depth) -> tuple[bool, int] | tuple[bool, None]:

        if from_node == to_node:
            return True, depth

        visited.add(from_node)
        for node in self._edges[from_node]:
            if node not in visited:
                has_path, path_depth = self._dfs_rec_with_depth(node, to_node, visited, depth+1)
                if has_path:
                    return True, path_depth
        return False, None

    def dfs_with_paths(self, from_node, to_node):
        path = [from_node]
        all_paths = []
        self._dfs_rec_with_paths(from_node, to_node, set(), path, all_paths)
        print(f"All paths: {all_paths}")
        return path

    def _dfs_rec_with_paths(
            self, from_node, to_node,
            visited, path: list, all_paths: list) -> bool:

        if from_node == to_node:
            all_paths.append(path.copy())
            return True

        visited.add(from_node)

        for node in self._edges[from_node]:
            if node not in visited:
                path.append(node)
                self._dfs_rec_with_paths(node, to_node, visited, path, all_paths)
                path.pop()

        return False



    def __str__(self):
        return self._edges


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
    graph.add_edge('Hong Kong', 'London')

    graph.add_edge('Paris', 'Amsterdam')
    graph.add_edge('Paris', 'London')

    pprint.pprint(graph._edges)

    # print(f"Path from Brussels to Amsterdam: {graph.bfs('Brussels', 'Amsterdam')}")
    # print(f"Path from Tokyo to Brussels: {graph.bfs('Tokyo', 'Brussels')}")

    # print(f"Path from Brussels to Amsterdam: {graph.dfs('Brussels', 'Amsterdam')}")
    # print(f"Path from Tokyo to Brussels: {graph.dfs('Tokyo', 'Brussels')}")

    # print(f"Path from Brussels to Amsterdam: {graph.dfs_with_depth('Brussels', 'Amsterdam')}")
    # print(f"Path from Tokyo to Brussels: {graph.dfs_with_depth('Tokyo', 'Brussels')}")

    print(f"Path from Brussels to Amsterdam: {graph.dfs_with_paths('Tokyo', 'London')}")
    # print(f"Path from Tokyo to Brussels: {graph.dfs_with_depth('Tokyo', 'Brussels')}")



