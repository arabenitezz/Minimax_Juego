# tablero.py

import pygame  # Importa el módulo pygame para manejar gráficos y eventos
from .constantes import BLACK, WHITE, CELL_SIZE, GRID_SIZE  # Importa constantes de otro módulo en el mismo paquete

def draw_grid(screen): # screen es el objeto de superficie de Pygame donde se dibujará el tablero.
    for row in range(GRID_SIZE):  # Recorre cada fila de la cuadrícula
        for col in range(GRID_SIZE):  # Recorre cada columna de la cuadrícula
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)  # Define un rectángulo para la celda
            if (row + col) % 2 == 0: # = 0 habla del residuo de la division 
                #col * CELL_SIZE calcula la coordenada x de la celda actual.
                # row * CELL_SIZE calcula la coordenada y de la celda actual.
                # CELL_SIZE es el tamaño (ancho y alto) de cada celda.
                # pygame.Rect crea un objeto Rect con estas coordenadas y dimensiones.
                # (row + col) % 2 se utiliza para alternar los colores.
                # Si la suma es impar, la celda es blanca.
                pygame.draw.rect(screen, WHITE, rect)  # Dibuja la celda de color blanco
            else:
                pygame.draw.rect(screen, BLACK, rect)  # Dibuja la celda de color negro
                # pygame.draw.rect dibuja un rectángulo con el color y las coordenadas/dimensiones especificadas en rect.
                # Si la suma de la fila y la columna es par ((row + col) % 2 == 0), la celda es blanca.

