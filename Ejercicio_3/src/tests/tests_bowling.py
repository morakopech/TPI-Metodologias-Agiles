from src.bowling import Juego

def test_loser():
    game = Juego()
    for tiro in range(20):
        game.Tirar(0)
    assert game.Score()==0

def test_todos_1():
    game = Juego()
    for tiro in range(20):
        game.Tirar(1)
    assert game.Score()==20

def test_un_spare():
    """Probar que al menos haya un Spare"""
    game = Juego()
    for tiro in range(20):
        game.Tirar(tiro)
    assert game.Score() == 29


def test_un_strike():
    """Probar que haya al menos un Strike"""
    game = Juego()

def test_juego_perfecto():
    """Probar el juego perfecto"""
    game = Juego()


