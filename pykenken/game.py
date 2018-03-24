import numpy as np


def random_board(size):
    """
    Creates a randomly generated board where there are no duplicates
    in each row/column
    """
    # Integers that control the values
    vals = list(range(1, size + 1))

    # TODO: Redo this
    board = np.zeros((size, size), dtype=int)
    for row in range(size):
        while True:
            board[row, :] = 0
            for col in range(size):
                possible = set(vals) - set(list(board[row, :]) + list(board[:, col]))

                if len(possible) == 0:
                    break
                board[row, col] = np.random.choice(list(possible))
            else:
                break
    return board


def partition_board(size, num_partitions, max_partition_size, min_partition_size):
    """
    Partitions a board size into a set of groups
    """
    # TODO: Clean up this logic
    partitions = []

    # Create a graph like structure that is initialized with the size x size board
    # size*size list with elements (position, connections)
    graph = [(i, [i-1, i+1, i-size, i+size]) for i in range(size*size)]
    graph_map = {i: i for i in range(size*size)}

    # Remove the connections that are off the board
    for g in graph:
        g[1] = [i for i in g[1] if i > 0 and i < size*size]

    # Randomly join together graph elements until we are satisfied with our conditions
    while True:
        # Element to join
        g = np.random.choice(graph)
        # Vertex to add on
        v = np.random.choice(g[1])

        graph_to_merge_with = graph[graph_map[v]]

        # Merge together




    return partitions


class KenKen(object):
    def __init__(self):
        # Groups are dicts with 'coords', 'operation', and 'value'
        self._groups = []

        # Board is a 2d array that just stores the correct answers
        self._board = None

    @classmethod
    def generate(cls, size: int, **kwargs):
        # kwargs to control rough difficulty settings

        result = cls()

        # Start the generation by creating a random 2d board state
        # That does not have duplicates in any row or column
        result._board = random_board(size)

        # Next partition the board into a set of connected groups

        return result

    @property
    def board(self):
        return self._board