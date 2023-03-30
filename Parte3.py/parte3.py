import csv
import pandas as pd

#CLASE POKEMON
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
            
            
 #weapon_attack
        def daño_cada_arma(self):
            if self.Tipo_arma=="codazo":
                return 2
            elif self.Tipo_arma=="patada":
                return 1.5
            elif self.Tipo_arma=="puñetazo":
                return 4
            elif self.Tipo_arma=="cabezazo":
                return 3



#fight_attack
        def atacar(self, pokemon,pokemon_a_atacar):
            if self.esta_vivo()==True:#si el pokemon que ataca esta vivo
                if pokemon_a_atacar.esta_vivo()==True:#si el pokemon que ataca esta vivo
                    if self.Tipo_arma=="codazo":
                        pokemon_a_atacar.Puntos_salud=pokemon_a_atacar.Puntos_salud-(self.Indice_ataque*self.daño_cada_arma())
                        print("El pokemon",pokemon.Nombre,"ha atacado al pokemon",pokemon_a_atacar.Nombre,"y le ha quitado",self.Indice_ataque*self.daño_cada_arma(),"puntos de salud")
                    elif self.Tipo_arma=="patada":
                        pokemon_a_atacar.Puntos_salud=pokemon_a_atacar.Puntos_salud-(self.Indice_ataque*self.daño_cada_arma())
                        print("El pokemon",pokemon.Nombre,"ha atacado al pokemon",pokemon_a_atacar.Nombre,"y le ha quitado",self.Indice_ataque*self.daño_cada_arma(),"puntos de salud")
                    elif self.Tipo_arma=="puñetazo":
                        pokemon_a_atacar.Puntos_salud=pokemon_a_atacar.Puntos_salud-(self.Indice_ataque*self.daño_cada_arma())
                        print("El pokemon",pokemon.Nombre,"ha atacado al pokemon",pokemon_a_atacar.Nombre,"y le ha quitado",self.Indice_ataque*self.daño_cada_arma(),"puntos de salud")
                    elif self.Tipo_arma=="cabezazo":
                        pokemon_a_atacar.Puntos_salud=pokemon_a_atacar.Puntos_salud-(self.Indice_ataque*self.daño_cada_arma())
                        print("El pokemon",pokemon.Nombre,"ha atacado al pokemon",pokemon_a_atacar.Nombre,"y le ha quitado",self.Indice_ataque*self.daño_cada_arma(),"puntos de salud")
                else:
                    print("El pokemon",pokemon_a_atacar.Nombre,"esta muerto")
            else:
                print("El pokemon",pokemon.Nombre,"esta muerto")


#is alive
        def esta_vivo(self):
            if self.Puntos_salud>0:
                return True
            else:
                return False



#CLASE ENTRENADOR

class Entrenador:
    def __init__(self,nombre,pokemons):
        self.nombre=nombre
        self.pokemons=pokemons
    def elegir_pokemon(self):
        pokemon_seleccionado=None
        while not pokemon_seleccionado:#mientras no haya pokemon seleccionado
            print("Entrenador",self.nombre,"elija un pokemon")
            for i,pokemon in  enumerate(self.pokemons):#recorremos los pokemons del entrenador y los enumeramos
                print(str(i+1)+".",pokemon.Nombre + " con " + str(pokemon.Puntos_salud) + " puntos de salud")#mostramos los pokemons del entrenador
            pokemon_seleccionado=int(input("Elige un pokemon:"))#seleccionamos un pokemon

            if pokemon_seleccionado>len(self.pokemons) or pokemon_seleccionado<1:#si el pokemon seleccionado no esta en la lista
                print("El pokemon seleccionado no esta en la lista")
                pokemon_seleccionado=None#vuelve a pedir un pokemon
            else:
                pokemon_seleccionado=self.pokemons[pokemon_seleccionado-1]
            if not pokemon_seleccionado.esta_vivo():
                print("El pokemon seleccionado esta muerto")
                pokemon_seleccionado=None
                print(self.nombre,"ha seleccionado a",pokemon_seleccionado.Nombre)
        return pokemon_seleccionado
        





   



