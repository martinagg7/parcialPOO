from parte3 import *

import csv
if __name__=="main":
    def leer_pokemons_entrenadores(ruta_archivo):
        pokemons=[]
        with open(ruta_archivo) as archivo:
            lector=csv.reader(archivo)
            for linea in lector:
                ID,Nombre,Tipo_arma,Puntos_salud,Indice_ataque,Indice_defensa=linea
                pokemon=Pokemon(ID,Nombre,Tipo_arma,Puntos_salud,Indice_ataque,Indice_defensa)
                pokemons.append(pokemon)
        return pokemons

    def datos_entrenadores():
        ruta_archivo_1="/Users/martinagarciagonzalez/Downloads/ajedrez_final-main/estructura de datos y algortimos/1_coach.csv"
        ruta_archivo_2="/Users/martinagarciagonzalez/Downloads/ajedrez_final-main/estructura de datos y algortimos/2_coach.csv"
    
        pokemons_coach_1=leer_pokemons_entrenadores(ruta_archivo_1)
        pokemons_coach_2=leer_pokemons_entrenadores(ruta_archivo_2)



