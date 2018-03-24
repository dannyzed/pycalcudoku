from pykenken.game import KenKen
from pykenken.visualize import save_figure


def test_save_figure():
    game = KenKen.generate(5)

    save_figure(game, 'test.png', solution=True)