
def presentacion():
    print("Estos son los dos entrenadores que se enfrentaran:")
    #presentamos los pokemos de los dos coaches
    import pandas as pd 
    datos1=pd.read_csv('1_coach.csv')
    print("----------------------------------------datos del coach 1---------------------------")
    print(datos1)

    datos2=pd.read_csv('2_coach.csv')
    print("----------------------------------------datos del coach 2---------------------------")
    print(datos2)

#ahora vamos a guardar los datos de los pokemos en una lista

#COACH 1
import csv
with open('1_coach.csv', 'r') as file:
    datos=file.readlines()
    datos.pop(0)#eliminamos la primera linea
    datos_coach1=[]
    for i in datos:
        pokemon=i.strip().split(',')
        datos_coach1.append(pokemon)
pokemon1_1=datos_coach1[0]
pokemon1_coach1=tuple(pokemon1_1)
pokemon1_2=datos_coach1[1]
pokemon2_coach1=tuple(pokemon1_2)
pokemon1_3=datos_coach1[2]
pokemon3_coach1=tuple(pokemon1_3)


#COACH 2
import csv
with open('2_coach.csv', 'r') as file:
    datos=file.readlines()
    datos.pop(0)#eliminamos la primera linea
    datos_coach2=[]
    for i in datos:
        pokemon=i.strip().split(',')
        datos_coach2.append(pokemon)
pokemon2_1=datos_coach2[0]
pokemon1_coach2=tuple(pokemon2_1)
pokemon2_2=datos_coach2[1]
pokemon2_coach2=tuple(pokemon2_2)
pokemon2_3=datos_coach2[2]
pokemon3_coach2=tuple(pokemon2_3)


#ahora vamos a crear las listas de los pokemon de cada coach
def lista_pokemons_coach1():
    pokemon1_1=datos_coach1[0]
    pokemon1_2=datos_coach1[1]
    pokemon1_3=datos_coach1[2]

def lista_pokemons_coach2():
    pokemon2_1=datos_coach2[0]
    pokemon2_2=datos_coach2[1]
    pokemon2_3=datos_coach2[2]



    

