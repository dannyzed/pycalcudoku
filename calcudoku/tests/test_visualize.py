from calcudoku.game import Calcudoku
from calcudoku.visualize import save_figure


def test_save_figure():
    game = Calcudoku.generate(6)

    save_figure(game, 'puzzle.png', solution=False)
    save_figure(game, 'puzzle_solution.png', solution=True)