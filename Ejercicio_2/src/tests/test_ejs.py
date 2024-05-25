from src.ejs import Sumar

def test_suma_vacia():
    assert Sumar("") == 0

def test_suma_nros():
    assert Sumar("1,2") == 3
    assert Sumar("4,2") == 6

def test_suma_3_nros():
    assert Sumar("3,8,7") == 18

def test_suma_con_nuevas_lineas():
    assert Sumar("1,2,4\n5,6") == 18

def test_suma_con_delimitador_configurable():
    assert Sumar("//;\n1;3;6;4") == 14
    assert Sumar("//|\n1|3|6|4") == 14

#def test_sumar_con_negativo():
    #assert Sumar("1,-3,6,4")
