from pykenken.game import KenKen
import numpy as np


def test_generate_board_unique():
    size = 6
    kenken = KenKen.generate(size)

    for row in kenken.board:
        np.testing.assert_equal(np.sort(row), np.unique(row))

    for col in kenken.board.T:
        np.testing.assert_equal(np.sort(col), np.unique(col))