from src.main import sum, multiplicar

def test_sum():
    assert sum(2,5) == 7 

def test_multip():
    assert multiplicar(3,4) == 12