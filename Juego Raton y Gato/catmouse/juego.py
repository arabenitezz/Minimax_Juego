# juego.py

import pygame  # Importa el módulo pygame para manejar gráficos y eventos
import sys  # Importa el módulo sys para manejar la salida del programa
from .constantes import *  # Importa todas las constantes desde el modulo constantes
from .tablero import draw_grid # Importa la función draw_grid desde el módulo tablero
from .piezas import Pieza, PiezaMinimax # Importa las clases Pieza y PiezaMinimax desde el módulo piezas

class Juego:
    def init(self):
        pygame.init() # Inicializa todos los módulos de Pygame
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Crea la ventana del juego con las dimensiones especificadas
        pygame.display.set_caption("Cat Mouse") # Establece el título de la ventana
        self.clock = pygame.time.Clock() # Crea un objeto Clock para controlar la velocidad del juego
        # Con Clock, el juego se ejecuta a una velocidad constante en diferentes dispositivos, lo que garantiza una experiencia de juego uniforme para todos los jugadores.
        # Controlar la velocidad de fotogramas evita que el juego utilice más recursos de los necesarios en sistemas más potentes, lo que puede provocar un sobrecalentamiento o un consumo innecesario de energía en dispositivos móviles, por ejemplo.
        self.gato = PiezaMinimax(GATO_IMG, [0, 0]) # Crea una instancia de PiezaMinimax para el gato con su posición inicial
        self.raton = Pieza(RATON_IMG, [4, 4]) # Crea una instancia de Pieza para el ratón con su posición inicial
        self.turno = "raton" # Establece que el turno inicial es del ratón
        self.turn_count = 0 # Inicializa el contador de turnos en 0

    def verificar_ganador(self):
        if self.gato.position == self.raton.position:  # Si el gato ha atrapado al ratón
            print('El gato ha atrapado al ratón')  # Imprime un mensaje
            pygame.quit()  # Cierra Pygame
            sys.exit()  # Sale del programa
        elif self.turn_count >= 5:  # Si han pasado 5 turnos
            print("¡El ratón ha sobrevivido 5 turnos! ¡Gana el ratón!")  # Imprime un mensaje
            pygame.quit()  # Cierra Pygame
            sys.exit()  # Sale del programa

    def dibujar(self):
        self.screen.fill(BLACK)  # Rellena la pantalla con el color negro # se utiliza para preparar la pantalla antes de dibujar
        # los elementos del juego en cada fotograma, garantizando una representación visual limpia y coherente del juego en cada momento.
        draw_grid(self.screen)  # Dibuja la cuadrícula en la pantalla
        self.gato.draw(self.screen)  # Dibuja el gato en la pantalla
        self.raton.draw(self.screen)  # Dibuja el ratón en la pantalla
        pygame.display.flip()  # Actualiza la pantalla para mostrar los cambios

    def manejar_eventos(self):
        for event in pygame.event.get():  # Itera sobre los eventos en la cola de eventos
            if event.type == pygame.QUIT:  # Si se cierra la ventana
                pygame.quit()  # Cierra Pygame
                sys.exit()  # Sale del programa
            elif event.type == pygame.KEYDOWN:  # Si se presiona una tecla
                if self.turno == "raton":  # Si es el turno del ratón
                    if event.key == pygame.K_UP:
                        self.raton.move("UP")  # Mueve el ratón hacia arriba
                        self.turno = "gato"  # Cambia el turno al gato
                    elif event.key == pygame.K_DOWN:
                        self.raton.move("DOWN")  # Mueve el ratón hacia abajo
                        self.turno = "gato"  # Cambia el turno al gato
                    elif event.key == pygame.K_LEFT:
                        self.raton.move("LEFT")  # Mueve el ratón hacia la izquierda
                        self.turno = "gato"  # Cambia el turno al gato
                    elif event.key == pygame.K_RIGHT:
                        self.raton.move("RIGHT")  # Mueve el ratón hacia la derecha
                        self.turno = "gato"  # Cambia el turno al gato
                self.turn_count += 1  # Incrementa el contador de turnos

    def ejecutar(self):
        self.init()
        running = True  # Establece que el juego está en ejecución
        while running:  # Bucle principal del juego
            self.manejar_eventos()  # Maneja los eventos del juego
            if self.turno == "gato":  # Si es el turno del gato
                self.gato.move_minimax(self.raton.position)  # Mueve el gato usando el algoritmo minimax
                self.turno = "raton"  # Cambia el turno al ratón

            self.verificar_ganador()  # Verifica si hay un ganador
            self.dibujar()  # Dibuja el estado actual del juego en la pantalla
            self.clock.tick(30)  # Controla la velocidad del bucle del juego
            # asegura que el bucle principal del juego se ejecute aproximadamente 30 veces por segundo, proporcionando una experiencia de juego suave y constante.
            # Si el hardware del sistema es más lento y el juego no puede alcanzar 30 fotogramas por segundo, tick()
            # espera más tiempo entre fotogramas para mantener la velocidad de fotogramas deseada.

        pygame.quit()  # Cierra Pygame
        sys.exit()  # Sale del programa













