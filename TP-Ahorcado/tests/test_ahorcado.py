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
    


def test_iniciar_jugada():
    juego = Ahorcado()
    assert juego.intentos == 7
    assert juego.intentos_restantes == 7
    assert juego.letras_adivinadas == []


def test_intento_pass():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "esponja"
    assert juego.intento("e") == True
    assert juego.letras_adivinadas == ["e"]
    assert juego.intentos_restantes == 7
    
def test_intento_fail():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "esponja"
    assert juego.intento("z") == False
    assert juego.letras_adivinadas == []
    assert juego.intentos_restantes == 6
