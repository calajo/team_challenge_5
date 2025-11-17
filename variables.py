# Aqui definiremos las constantes del juego Hundir la Flota

# Dimensiones del tablero
DIMENSION_TABLERO = 10

# Definición de los barcos: nombre y eslora
BARCOS = {
    "portaviones": 4,  # 1 barco de 4 posiciones
    "submarino_1": 3,  # 2 barcos de 3 posiciones
    "submarino_2": 3,
    "destructor_1": 2,  # 3 barcos de 2 posiciones
    "destructor_2": 2,
    "destructor_3": 2,
    "lancha_1": 1,  # 4 barcos de 1 posición
    "lancha_2": 1,
    "lancha_3": 1,
    "lancha_4": 1
}

# Símbolos para el tablero
AGUA = " "  # Posición vacía
BARCO = "O"  # Posición con barco
IMPACTO = "X"  # Disparo que dio a un barco
FALLO = "-"  # Disparo al agua

# IDs de jugadores
JUGADOR_HUMANO = "Jugador"
JUGADOR_MAQUINA = "Máquina"
