import random

class Ahorcado():
    def __init__(self):
        self.palabra_vacia = ""
        self.palabra_a_adivinar = ""
    
    def rayitas(self, palabra):
        r = len(palabra)
        self.palabra_vacia = '_ ' * r
        return self.palabra_vacia.strip()  # Elimina el espacio extra al final de palabra_vacia
    
    def validar_letra(self, letra):
        if (letra in self.palabra_a_adivinar): return True
        else: return False
    
    def validar_palabra(self, palabra):
        if (palabra == self.palabra_a_adivinar): return True
        else: return False