# funciones.py
import random
from variables import *


def mostrar_bienvenida():
    print("=" * 50)
    print("    ¡BIENVENIDO A HUNDIR LA FLOTA THE BRIDGE!")
    print("=" * 50)
    print("\nINSTRUCCIONES:")
    print("- El tablero es de 10x10 (filas 0-9, columnas 0-9)")
    print("- Debes hundir todos los barcos de tu oponente, una máquina")
    print("- Si aciertas, vuelves a disparar")
    print("- Si fallas, le toca a tu oponente, la máquina")
    print("- La máquina también disparará si acierta")
    print("\nSÍMBOLOS:")
    print(f"  {AGUA} = Agua / No disparado")
    print(f"  {BARCO} = Tu barco")
    print(f"  {IMPACTO} = Impacto")
    print(f"  {FALLO} = Fallo")
    print("\nBARCOS EN JUEGO:")
    print("  - 1 Portaviones (4 posiciones)")
    print("  - 2 Submarinos (3 posiciones cada uno)")
    print("  - 3 Destructores (2 posiciones cada uno)")
    print("  - 4 Lanchas (1 posición cada una)")
    print("\nRecuerda, los Barcos pueden estar colocados horizontalmente o verticalmente")
    print("\n" + "=" * 50)
    input("\nPresiona ENTER para comenzar...")


def obtener_coordenadas():
    try:
        fila = int(input("\nIntroduce la fila (0-9): "))
        columna = int(input("Introduce la columna (0-9): "))
        
        if 0 <= fila < DIMENSION_TABLERO and 0 <= columna < DIMENSION_TABLERO:
            return (fila, columna)
        else:
            print("Coordenadas fuera del tablero. Recuerda el valor debe estar entre 0 y 9. Lo siento, pero has perdido el turno")
            return None
    except ValueError:
        print("Por favor, introduce números válidos.")
        return None


def disparo_aleatorio_maquina(tablero_jugador):
    intentos = 0
    max_intentos = 1000
    
    while intentos < max_intentos:
        fila = random.randint(0, DIMENSION_TABLERO - 1)
        columna = random.randint(0, DIMENSION_TABLERO - 1)
        
        # Verificar que no se haya disparado ya en esa posición
        if tablero_jugador.tablero_disparos[fila][columna] == AGUA:
            return (fila, columna)
        
        intentos += 1
    
    # Si no encuentra posición (caso muy raro), buscar la primera disponible
    for i in range(DIMENSION_TABLERO):
        for j in range(DIMENSION_TABLERO):
            if tablero_jugador.tablero_disparos[i][j] == AGUA:
                return (i, j)
    
    return None


def turno_jugador(tablero_maquina):
    print("\n" + "=" * 50)
    print("TU TURNO")
    print("=" * 50)
    
    # Mostrar el tablero de disparos del jugador (lo que ve del enemigo)
    print("\nTablero enemigo (tus disparos):")
    tablero_maquina.mostrar_tablero(mostrar_barcos=False)
    
    # Obtener coordenadas
    coordenadas = obtener_coordenadas()
    
    if coordenadas is None:
        return None
    
    fila, columna = coordenadas
    
    # Disparar
    resultado = tablero_maquina.disparar(fila, columna)
    
    if resultado is None:
        print("Ya has disparado en esa posición. Intenta otra.")
        return None
    elif resultado:
        print(f"¡IMPACTO en ({fila}, {columna})!")
        return True
    else:
        print(f"Agua en ({fila}, {columna})")
        return False


def turno_maquina(tablero_jugador):
    print("\n" + "=" * 50)
    print("TURNO DE LA MÁQUINA")
    print("=" * 50)
    
    coordenadas = disparo_aleatorio_maquina(tablero_jugador)
    
    if coordenadas is None:
        print("La máquina no tiene más posiciones donde disparar")
        return False
    
    fila, columna = coordenadas
    
    resultado = tablero_jugador.disparar(fila, columna)
    
    if resultado:
        print(f"¡La máquina IMPACTÓ tu barco en ({fila}, {columna})!")
        return True
    else:
        print(f"La máquina disparó al agua en ({fila}, {columna})")
        return False


def mostrar_estado_juego(tablero_jugador, tablero_maquina):
    print("\n" + "=" * 50)
    print("ESTADO DEL JUEGO")
    print("=" * 50)
    
    # Tablero del jugador (con sus barcos)
    print("\nTU TABLERO:")
    tablero_jugador.mostrar_tablero(mostrar_barcos=True)
    print(f"Posiciones de barco que te quedan: {tablero_jugador.posiciones_barco}")
    
    # Tablero enemigo (solo disparos)
    print("\nTABLERO ENEMIGO (tus disparos):")
    tablero_maquina.mostrar_tablero(mostrar_barcos=False)
    print(f"Posiciones de barco enemigas que te faltan por hundir: {tablero_maquina.posiciones_barco}")
