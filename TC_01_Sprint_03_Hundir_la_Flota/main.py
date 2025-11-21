from tablero import Tablero
from funciones import *
from variables import *


def main():  
    # Aqui se muestra la bienvenida e instrucciones para participar
    mostrar_bienvenida()
    
    # Aqui se inicializan los tableros
    print("\n Se estan colocando barcos...")
    tablero_jugador = Tablero(JUGADOR_HUMANO)
    tablero_maquina = Tablero(JUGADOR_MAQUINA)
    print("¡Todo listo!")
    
    # Mostramos el estado inicial
    mostrar_estado_juego(tablero_jugador, tablero_maquina)
    
    # Bucle del juego y empieza siempre el jugador, no se ha realizado a suerte, podría ser un Random
    juego_activo = True
    turno_actual = "jugador" 
    
    while juego_activo:
        if turno_actual == "jugador":
            resultado = turno_jugador(tablero_maquina)
            if resultado:
                # Se ha acertado, por lo que debe seguir el jugador
                print("¡Sigue siendo tu turno!")
                
                # Aqui se verifica si se ha finalziado la partida
                if not tablero_maquina.quedan_barcos():
                    print("\n" + "=" * 60)
                    print("¡FELICIDADES! ¡HAS GANADO LA PARTIDA!")
                    print("=" * 60)
                    tablero_maquina.mostrar_tablero(mostrar_barcos=True)
                    juego_activo = False
            else:
                # Fallo, el turno es de la máquina
                print("Es el turno de la máquina")
                turno_actual = "maquina"
                input("\nPresiona ENTER para continuar...")
        
        else:
            resultado = turno_maquina(tablero_jugador)
            if resultado:
                # Se ha acertado, por lo que debe seguir la máquina
                print("La máquina vuelve a disparar...")
                
                # Aqui se verifica si se ha finalziado la partida
                if not tablero_jugador.quedan_barcos():
                    print("\n" + "=" * 60)
                    print("FIN DE LA PARTIDA - La máquina ha ganado")
                    print("=" * 60)
                    tablero_jugador.mostrar_tablero(mostrar_barcos=True)
                    juego_activo = False
                else:
                    input("\nPresiona ENTER para continuar...")
            else:
                # Fallo, el turno es del jugador
                print("Es tu turno de nuevo")
                turno_actual = "jugador"
                mostrar_estado_juego(tablero_jugador, tablero_maquina)
    
    # Fin del juego
    print("\n¡Gracias por jugar!")
    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
