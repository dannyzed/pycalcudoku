import numpy as np
from pykenken.graph import Graph


def identity(x):
    return x[0]


def divide(x):
    if max(x) % min(x) == 0:
        return max(x) / min(x)
    else:
        return np.nan


def subtract(x):
    return np.abs(x[1] - x[0])

# Possible operations that can be done on a partition
# (min_elements, max_elements, function)
OPERATIONS = {
    'divide': (2, 2, divide),
    'multiply': (2, np.inf, np.multiply.reduce),
    'add': (2, np.inf, np.add.reduce),
    'subtract': (2, 2, subtract),
    'none': (1, 1, identity),
}

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
    return board.flatten()


def partition_board(size, num_partitions, max_partition_size, min_partition_size):
    """
    Partitions a board size into a set of groups
    """
    # TODO: Clean up this logic
    graph = Graph(size)

    # Repeatedly merge nodes of the graph until some conditions are satisfied
    for idx in range(30):
        node_idx = np.random.choice(list(range(len(graph.nodes))))

        merge_node = np.random.choice(graph.edges[node_idx])
        try:
            merge_idx = graph.nodes.index(merge_node)
        except ValueError:
            # Should not happen
            raise ValueError

        if len(graph.nodes[node_idx].coords) + len(merge_node.coords) > max_partition_size:
            continue

        graph.merge(node_idx, merge_idx)

    partitions = [n.coords for n in graph.nodes]

    return partitions


def possible_operations(partitions):
    all_possibles = []
    for partition in partitions:
        possibles = []

        for name, (min_size, max_size, operation) in OPERATIONS.items():
            if min_size <= len(partition) <= max_size:
                val = operation(partition)
                if ~np.isnan(val):
                    possibles.append((name, val))
        all_possibles.append(possibles)
    return all_possibles


class KenKen(object):
    def __init__(self):
        # Groups are dicts with 'coords', 'operation', and 'value'
        self._groups = []

        # Board is a 2d array that just stores the correct answers
        self._board = None

        # Partitions looks like [[1, 4, 5], [2], ...] which stores the connections
        # of the board coordinates
        self._partitions = None

        # Operations stores the game state, [('divide', 4), ('add', 7), ...]
        # What each partition corresponds to in the game
        self._operations = None

    @classmethod
    def generate(cls, size: int, **kwargs):
        # kwargs to control rough difficulty settings

        result = cls()

        # Start the generation by creating a random 2d board state
        # That does not have duplicates in any row or column
        result._board = random_board(size)

        # Next partition the board into a set of connected groups
        partitions = partition_board(size, 10, 4, 1)

        # Get the values corresponding to each partition location
        partition_values = []
        for p in partitions:
            partition_values.append([result._board[v] for v in p])

        possibles = possible_operations(partition_values)

        # Choose a random possible operation for each partition
        # TODO: Proper logic here
        chosen = []
        for possible in possibles:
            # Funny things happen when taking random.choice of a list of tuples
            random_index = np.random.choice(list(range(len(possible))))
            chosen.append(possible[random_index])

        result._partitions = partitions
        result._operations = chosen

        return result

    @property
    def board(self):
        return self._board

    @property
    def partitions(self):
        return self._partitions

    @property
    def operations(self):
        return self._operations