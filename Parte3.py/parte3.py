import csv
import pandas as pd

class Pokemon:
        IDS=[]
    #constructor
        def __init__(self, ID,Nombre,Tipo_arma,Puntos_salud,Indice_ataque,Indice_defensa):
    #ajustamos los valores dando error cuando sea preciso
            if ID in Pokemon.IDS:
                raise ValueError("El ID ya existe")
            armas=["codazo","patada","puñetazo","cabezazo"]
            if Tipo_arma not in armas:
                raise ValueError("El tipo de arma debe ser codazo, patada, puñetazo o cabezazo")
            if Puntos_salud>100 or Puntos_salud<1:
                raise ValueError("Los puntos de salud deben estar entre 1 y 100")
            if Indice_ataque>10 or Indice_ataque<1:
                raise ValueError("El indice de ataque debe estar entre 1 y 100")
            if Indice_defensa>10 or Indice_defensa<1:
                raise ValueError("El indice de defensa debe estar entre 1 y 100")
            
    #atributos pokemon
            self.ID=ID
            self.Nombre=Nombre
            self.Puntos_salud=Puntos_salud
            self.Indice_ataque=Indice_ataque
            self.Indice_defensa=Indice_defensa
            self.Tipo_arma=Tipo_arma
            