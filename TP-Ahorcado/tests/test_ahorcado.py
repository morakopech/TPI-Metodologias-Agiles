from ahorcado import *

def test_cant_rayitas():
    juego = Ahorcado()
    assert juego.rayitas("Botella") == "_ _ _ _ _ _ _"

def test_cant_rayitas2():
    juego = Ahorcado()
    assert juego.rayitas("cargador") == "_ _ _ _ _ _ _ _"

