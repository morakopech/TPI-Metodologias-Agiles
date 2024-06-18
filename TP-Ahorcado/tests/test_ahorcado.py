from ahorcado import *

def test_cant_rayitas():
    juego = Ahorcado()
    assert juego.rayitas("Botella") == "_ _ _ _ _ _ _"

def test_cant_rayitas2():
    juego = Ahorcado()
    assert juego.rayitas("cargador") == "_ _ _ _ _ _ _ _"

def test_cant_rayitas3():
    juego = Ahorcado()
    assert juego.rayitas("computadora") == "_ _ _ _ _ _ _ _ _ _ _"

def test_letra_correcta():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "hamaca"
    assert juego.validar_letra("a") == True
    
def test_letra_incorrecta():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "hamaca"
    assert juego.validar_letra("e") == False
    
def test_palabra_correcta():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "hamaca"
    assert juego.validar_palabra("hamaca") == True
    
def test_palabra_incorrecta():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "hamaca"
    assert juego.validar_palabra("calesita") == False
    