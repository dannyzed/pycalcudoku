import numpy as np


class Graph(object):
    def __init__(self, size: int):
        self._nodes = [Node(i) for i in range(size*size)]

        self._edges = []
        for n in range(size*size):
            self._edges.append([self._nodes[i] for i in [n-1, n+1, n-size, n+size] if i >= 0 and i < size*size])

    def merge(self, one, two):
        new_edges = list(set(self._edges[one] + self._edges[two]))

        self._nodes[one].add(self._nodes[two])

        new_edges.remove(self._nodes[one])
        new_edges.remove(self._nodes[two])

        self._edges[one] = new_edges

        del self._nodes[two]
        del self._edges[two]

    @property
    def nodes(self):
        return self._nodes

    @property
    def edges(self):
        return self._edges


class Node(object):
    def __init__(self, start):
        self._coords = [start]

    def __repr__(self):
        return 'Coords: ' + str(self.coords)

    @property
    def coords(self):
        return self._coords

    def add(self, node):
        self._coords += node.coords

    def __eq__(self, other):
        return self.coords == other.coords

    def __hash__(self):
        return hash(str(self.coords))