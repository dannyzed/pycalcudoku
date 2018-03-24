import numpy as np
from pykenken.graph import Graph


def test_graph_construction():
    g = Graph(5)


def test_graph_merge():
    g = Graph(5)

    g.merge(0, 1)

    np.testing.assert_equal(g.nodes[0].coords, [0, 1])

    np.testing.assert_equal(g.edges[0], [g.nodes[1], g.nodes[4], g.nodes[5]])
