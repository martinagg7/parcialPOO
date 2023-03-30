import random

#definimos los distintos tipos de pokemon
class Pokemon_Tierra:
    def __init__(self,Indice_defensa):
        if Indice_defensa<11 or Indice_defensa>20:
            raise ValueError('Indice_defensa debe estar entre 11 y 20')
        self.Indice_defensa=Indice_defensa
    
class Pokemon_Agua:
    def __init__(self,Indice_ataque):
        if Indice_ataque<11 or Indice_ataque>20:
            raise ValueError('Indice_ataque debe estar entre 11 y 20')
        self.Indice_ataque=Indice_ataque

class Pokemon_Aire:
    def Indice_defensa(self):
        if random.random()<=0.5:#50% de probabilidad de esquivar el ataque
            print("El pokemon",self.Nombre,"ha esquivado el ataque")
        else:
            print("El pokemon",self.Nombre,"ha sido atacado")

class Pokemon_Electrico:
    def Indice_ataque(self):
        if random.random()<=0.5:
            print("El ataque no ha sido efectivo")
        else:
            print("El ataque ha hecho el doble de daño")
