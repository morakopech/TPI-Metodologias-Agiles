from ahorcado import *

def test_cant_rayitas():
    juego = Ahorcado()
    assert juego.rayitas("Botella") == "_ _ _ _ _ _ _"
