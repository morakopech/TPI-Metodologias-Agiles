import random

class Ahorcado():
    def __init__(self):
        self.palabra_vacia = ""
        self.palabra_a_adivinar = ""
        self.intentos = 7
        self.intentos_restantes = 7
        self.letras_adivinadas = []
    
    def rayitas(self, palabra):
        r = len(palabra)
        self.palabra_vacia = '_ ' * r
        return self.palabra_vacia.strip()  # Elimina el espacio extra al final de palabra_vacia
    
    def validar_letra(self, letra):
        if (letra in self.palabra_a_adivinar): 
            self.letras_adivinadas += letra
            return True
        else:
            self.intentos_restantes -= 1
            return False
    
    def validar_palabra(self, palabra):
        if (palabra == self.palabra_a_adivinar): return True
        else: return False
        
    def intento(self,letra):
        print(letra)
        if (self.validar_letra(letra)):
            return True
        else:
            return False