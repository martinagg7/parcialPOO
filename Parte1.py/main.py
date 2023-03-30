from pokemon_presentacion import *
from clase_pokemon import *

if __name__ == "main":
    #probamos la clase pokemon
    presentacion()


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