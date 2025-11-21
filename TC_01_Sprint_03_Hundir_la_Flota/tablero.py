import numpy as np
import random
from variables import *


class Tablero:

    #   id_jugador: Identificador del jugador (ej: "Jugador", "Máquina")
    #   dimension: Tamaño del tablero (por defecto 10x10)
    #   barcos: Diccionario con los barcos y sus esloras

    def __init__(self, id_jugador, dimension=DIMENSION_TABLERO, barcos=BARCOS):

        self.id_jugador = id_jugador
        self.dimension = dimension
        self.barcos = barcos
        
        # Tablero con los barcos
        self.tablero_barcos = np.full((dimension, dimension), AGUA)
        
        # Tablero de disparos (para mostrar dónde se ha disparado)
        self.tablero_disparos = np.full((dimension, dimension), AGUA)
        
        # Contador de posiciones de barco restantes
        self.posiciones_barco = sum(barcos.values())
        
        # Colocar los barcos automáticamente
        self.colocar_barcos()
    
    def colocar_barcos(self):
        for nombre_barco, eslora in self.barcos.items():
            colocado = False
            intentos = 0
            # Con esto se evitan bucles infinitos
            max_intentos = 1000  
            
            while not colocado and intentos < max_intentos:
                # Elegir orientación aleatoria: 0=horizontal, 1=vertical
                orientacion = random.randint(0, 1)
                
                # Elegir posición inicial aleatoria
                if orientacion == 0:  # Horizontal
                    fila = random.randint(0, self.dimension - 1)
                    columna = random.randint(0, self.dimension - eslora)
                else:  # Vertical
                    fila = random.randint(0, self.dimension - eslora)
                    columna = random.randint(0, self.dimension - 1)
                
                # Verificar si se puede colocar el barco
                if self.puede_colocar_barco(fila, columna, eslora, orientacion):
                    self.colocar_barco_en_posicion(fila, columna, eslora, orientacion)
                    colocado = True
                
                intentos += 1
            
            if not colocado:
                print(f"Advertencia: No se ha podido colocar el barco {nombre_barco}")
    
    #   fila: Fila inicial
    #   columna: Columna inicial
    #   eslora: Tamaño del barco
    #   orientacion: 0=horizontal, 1=vertical
    def puede_colocar_barco(self, fila, columna, eslora, orientacion):
        # Horizontal
        if orientacion == 0:
            for c in range(columna, columna + eslora):
                if self.tablero_barcos[fila][c] != AGUA:
                    return False
        # Vertical
        else:
            for f in range(fila, fila + eslora):
                if self.tablero_barcos[f][columna] != AGUA:
                    return False
        
        return True
    
    def colocar_barco_en_posicion(self, fila, columna, eslora, orientacion):
        # Horizontal
        if orientacion == 0:
            for c in range(columna, columna + eslora):
                self.tablero_barcos[fila][c] = BARCO
        # Vertical
        else:
            for f in range(fila, fila + eslora):
                self.tablero_barcos[f][columna] = BARCO
    #   fila: Fila donde disparar
    #   columna: Columna donde disparar
    def disparar(self, fila, columna):
        # Verificar que las coordenadas son válidas
        if not (0 <= fila < self.dimension and 0 <= columna < self.dimension):
            return None
        
        # Verificar si ya se disparó en esta posición
        if self.tablero_disparos[fila][columna] != AGUA:
            return None
        
        # Comprobar si hay barco
        if self.tablero_barcos[fila][columna] == BARCO:
            self.tablero_disparos[fila][columna] = IMPACTO
            self.posiciones_barco -= 1
            return True
        else:
            self.tablero_disparos[fila][columna] = FALLO
            return False
    
    def quedan_barcos(self):
        #quedan barcos?
        return self.posiciones_barco > 0
    
    def mostrar_tablero(self, mostrar_barcos=False):
        #Si False se muestran los disparos solo
        print(f"\n  Tablero de {self.id_jugador}")
        print("  " + " ".join([str(i) for i in range(self.dimension)]))
        
        for i in range(self.dimension):
            fila = f"{i} "
            for j in range(self.dimension):
                if mostrar_barcos:
                    # Mostrar barcos y disparos
                    if self.tablero_disparos[i][j] == IMPACTO:
                        fila += IMPACTO + " "
                    elif self.tablero_disparos[i][j] == FALLO:
                        fila += FALLO + " "
                    elif self.tablero_barcos[i][j] == BARCO:
                        fila += BARCO + " "
                    else:
                        fila += AGUA + " "
                else:
                    # Solo mostrar disparos
                    fila += self.tablero_disparos[i][j] + " "
            
            print(fila)
        print("\n")
