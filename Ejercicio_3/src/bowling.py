class Juego:

    def __init__(self) -> None:
        self.jugada = 0
        self.tiros = []

    def Tirar(self, pinos:int):
        """Registra nro de pinos tumbados rn cada tiro"""
        self.jugada += 1
    
    def Score(self):
        """calcula y devuelve el puntaje total del juego"""
        return self.jugada
    

    