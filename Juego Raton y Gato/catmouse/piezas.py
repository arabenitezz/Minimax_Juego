
# piezas.py

import pygame  # Importa el módulo pygame para manejar gráficos y eventos
from .constantes import CELL_SIZE, GRID_SIZE # Importa constantes desde otro módulo en el mismo paquete
from minimax.algoritmo import get_possible_moves, minimax  # Importa funciones desde el módulo algoritmo en el paquete minimax

class Pieza:
    def __init__(self, image_path, initial_pos):
        self.image = pygame.image.load(image_path)  # Carga la imagen de la pieza
        # Esta línea carga la imagen desde la ruta especificada en image_path.
        # pygame.image.load(image_path) devuelve un objeto de superficie (Surface) de Pygame que contiene la imagen cargada.
        self.image = pygame.transform.scale(self.image, (CELL_SIZE, CELL_SIZE))  # Escala la imagen al tamaño de la celda
        # pygame.transform.scale es una función de Pygame que escala la superficie a un nuevo tamaño.
        # self.image es la superficie que se quiere escalar.
        # (CELL_SIZE, CELL_SIZE) es una tupla que especifica el nuevo ancho y alto al que se debe escalar la imagen.
        # Esta línea toma la imagen cargada y la redimensiona para que se ajuste al tamaño de una celda del tablero (CELL_SIZE x CELL_SIZE).
        self.position = initial_pos  # Establece la posición inicial de la pieza

    def draw(self, screen):
        screen.blit(self.image, (self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE))  # Dibuja la pieza en la pantalla

        #screen.blit es una función de Pygame que copia la superficie de una imagen (self.image) sobre otra superficie (screen), en este caso, la pantalla del juego.
        # self.position[0] * CELL_SIZE calcula la coordenada x donde se dibujará la imagen, multiplicando la posición x de la pieza por el tamaño de la celda.
        # self.position[1] * CELL_SIZE calcula la coordenada y donde se dibujará la imagen, multiplicando la posición y de la pieza por el tamaño de la celda.
        # (self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE) establece las coordenadas (x, y) en la pantalla donde se dibujará la imagen.

    def move(self, direction):
        new_position = self.position.copy()  # Copia la posición actual
        # self.position es la posición actual de la pieza en el tablero, representada como una lista [x, y].
        # self.position.copy() crea una copia de la lista para evitar modificar la posición original directamente.
        # new_position se usa para almacenar la nueva posición propuesta después del movimiento.
        if direction == "UP" and self.position[1] > 0:
            new_position[1] -= 1  # Mueve hacia arriba
        # Verifica si la dirección es "UP" y si la pieza no está en el borde superior del tablero (self.position[1] > 0).
        # Si es así, decrementa la coordenada y (new_position[1] -= 1), moviendo la pieza una celda hacia arriba.
        elif direction == "DOWN" and self.position[1] < GRID_SIZE - 1:
            new_position[1] += 1  # Mueve hacia abajo
        elif direction == "LEFT" and self.position[0] > 0:
            new_position[0] -= 1  # Mueve hacia la izquierda
        elif direction == "RIGHT" and self.position[0] < GRID_SIZE - 1:
            new_position[0] += 1  # Mueve hacia la derecha  
        # GRID_SIZE es una constante que define el tamaño del tablero (por ejemplo, 5 para un tablero de 5x5).
        # GRID_SIZE - 1 es el índice de la última fila del tablero. Por ejemplo, si GRID_SIZE es 5, entonces GRID_SIZE - 1 es 4, lo cual corresponde a la última fila del tablero (índices 0 a 4 para 5 filas).      
        if new_position != self.position:  # Si la nueva posición es diferente de la actual
            self.position = new_position  # Actualiza la posición de la pieza

class PiezaMinimax(Pieza):
    def move_minimax(self, target_pos):
        best_move = None  # Inicializa el mejor movimiento como None
        best_value = float('-inf')  # Inicializa el mejor valor como menos infinito # Iniciar con el valor más pequeño posible garantiza que cualquier evaluación será mejor que este valor inicial
        # Iniciamos con el peor valor posible para poder encontrar y actualizar con el máximo valor real evaluado durante el proceso.
        for move in get_possible_moves(self.position):  # Recorre los movimientos posibles
            move_value = minimax(3, False, move, target_pos)  # Llama al algoritmo minimax para evaluar el movimiento
            if move_value > best_value:  # Si el valor del movimiento es mejor que el mejor valor actual
                best_value = move_value  # Actualiza el mejor valor
                best_move = move  # Actualiza el mejor movimiento
        if best_move:  # Si existe un mejor movimiento
            self.position = best_move  # Actualiza la posición de la pieza

