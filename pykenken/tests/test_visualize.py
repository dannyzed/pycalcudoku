from pykenken.game import KenKen
from pykenken.visualize import save_figure


def test_save_figure():
    game = KenKen.generate(40)

    save_figure(game, 'kenken40.png', solution=False)
    save_figure(game, 'kenken40_solution.png', solution=True)