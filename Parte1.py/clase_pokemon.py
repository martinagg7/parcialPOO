from pokemon_presentacion import *

presentacion()

#Ahora vamos a crear la clase pokemon
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
    #destructor
            #def __del__(self):
               # print("El pokemon",self.Nombre,"ha sido eliminado")

    #metodos

        def info(self):
            return "El pokemon",self.ID,"se llama",self.Nombre,"tiene",self.Puntos_salud,"puntos de salud y su tipo de arma es",self.Tipo_arma
    #metodos get y set
        def ID(self):
            return self.ID
        def Nombre(self):
            return self.Nombre
        def Tipo_arma(self):
            return self.Tipo_arma
        def Puntos_salud(self):
            return self.Puntos_salud
        def Indice_ataque(self):
            return self.Indice_ataque
        def Indice_defensa(self):
            return self.Indice_defensa
    #is_alive
        def esta_vivo(self):
            if self.Puntos_salud>0:
                return True
            else:
                return False
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
    #fight_defense
        def defender(self, pokemon,pokemon_a_atacar):
            if pokemon.Indice_ataque<pokemon_a_atacar.Indice_defensa:
                return False
            else:
                return True
    






   
pokemon1_coach1=Pokemon(11,"Pikachu","codazo",69,8,8)
pokemon2_coach1=Pokemon(12,"Pidgey","patada",85,7,7)
pokemon3_coach1=Pokemon(13,"Squirtle","codazo",74,7,6)
pokemon1_coach2=Pokemon(24,"Diglett","puñetazo",82,9,7)
pokemon2_coach_2=Pokemon(25,"Venusaur","patada",78,8,6)
pokemon3_coach_2=Pokemon(26,"Charmeleon","codazo",88,9,7)
#descripcion

    #ataques aleatorios
pokemon1_coach1.atacar(pokemon1_coach1,pokemon1_coach2)
pokemon2_coach_2.atacar(pokemon2_coach_2,pokemon1_coach1)
pokemon3_coach_2.atacar(pokemon3_coach_2,pokemon3_coach_2)


    #descripcion
print("descripcion pokemon 1 coach1")
print(pokemon1_coach1.ID)
print(pokemon1_coach1.Nombre)
print(pokemon1_coach1.Tipo_arma)

    #defender
print("defensa pokemon 1 coach1 VS pokemon 1 coach2")
print(pokemon1_coach1.defender(pokemon1_coach1,pokemon1_coach2))
print("defensa pokemon 3 coach2 VS pokemon 1 coach1")
print(pokemon3_coach_2.defender(pokemon3_coach_2,pokemon1_coach1))
    #descripcion
print(pokemon1_coach1.info())
print(pokemon2_coach1.info())
print(pokemon3_coach1.info())
print(pokemon1_coach2.info())
