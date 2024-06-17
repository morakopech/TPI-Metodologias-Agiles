import random

class Ahorcado():
    def __init__(self):
        self.palabra_vacia = ""
    
    def rayitas(self, palabra):
        r = len(palabra)
        self.palabra_vacia = '_ ' * r
        return self.palabra_vacia.strip()  # Elimina el espacio extra al final de palabra_vacia
        
    