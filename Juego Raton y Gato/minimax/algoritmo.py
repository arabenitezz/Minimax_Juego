# algoritmo.py

from catmouse.constantes import GRID_SIZE  # Importa la constante GRID_SIZE desde el módulo constantes

def minimax(depth, is_maximizing_player, player_pos, target_pos):
    if depth == 0 or player_pos == target_pos:  # Condición de parada: profundidad 0 o el jugador alcanzó el objetivo
        return -distance(player_pos, target_pos)  # Devuelve el valor negativo de la distancia
    # Si la profundidad de búsqueda alcanza 0 o el jugador ha alcanzado la posición objetivo, se calcula y devuelve la
    # distancia negativa entre la posición del jugador y la posición objetivo. Esto permite que el algoritmo busque tanto
    # maximizar como minimizar la distancia al objetivo.

    if is_maximizing_player:  # Si es el jugador maximizador
        max_eval = float('-inf')  # Inicializa la mejor evaluación como menos infinito
        for move in get_possible_moves(player_pos):  # Recorre los movimientos posibles
            eval = minimax(depth - 1, False, move, target_pos)  # Llama recursivamente a minimax
            max_eval = max(max_eval, eval)  # Actualiza la mejor evaluación
        return max_eval  # Devuelve la mejor evaluación
    else:  # Si es el jugador minimizador
        min_eval = float('inf')  # Inicializa la mejor evaluación como infinito
        for move in get_possible_moves(target_pos):  # Recorre los movimientos posibles
            eval = minimax(depth - 1, True, player_pos, move)  # Llama recursivamente a minimax
            min_eval = min(min_eval, eval)  # Actualiza la mejor evaluación
        return min_eval  # Devuelve la mejor evaluación
    # El algoritmo se ejecuta recursivamente alternando entre dos modos: maximización y minimización, dependiendo del jugador que esté realizando el movimiento en el árbol de búsqueda.
    # En el modo de maximización (is_maximizing_player == True), el algoritmo busca el movimiento que maximiza la evaluación.
    # En el modo de minimización (is_maximizing_player == False), el algoritmo busca el movimiento que minimiza la evaluación.
    # El valor de evaluación es la distancia negativa entre las posiciones del jugador y del objetivo. En general, se quiere minimizar esta distancia.
    # Al maximizar este valor, se está minimizando la distancia entre el jugador y el objetivo, lo que es deseable para el jugador.
    # Al minimizar este valor, se está maximizando la distancia entre el jugador y el objetivo, lo que es deseable para el oponente.
    # Alternar entre maximización y minimización permite que la IA explore todas las posibles secuencias de movimientos tanto para el gato como para el ratón.
    # Esto asegura que la IA examine todas las opciones disponibles y seleccione la mejor acción posible en cada turno, maximizando sus posibilidades de éxito.
    # Cuando el objetivo es maximizar (por ejemplo, atrapar al ratón), la IA buscará los movimientos que maximicen su ventaja.
    # Cuando el objetivo es minimizar (por ejemplo, evitar que el ratón se escape), la IA buscará los movimientos que minimicen la ventaja del ratón.
def get_possible_moves(position):
    moves = []  # Inicializa la lista de movimientos posibles
    x, y = position  # Descompone la posición en coordenadas x e y
    if y > 0:
        moves.append([x, y - 1])  # Agrega el movimiento hacia arriba a la lista de movimientos posibles
    if y < GRID_SIZE - 1:
        moves.append([x, y + 1]) # Agrega el movimiento hacia abajo a la lista de movimientos posibles
    if x > 0:
        moves.append([x - 1, y]) # Agrega el movimiento hacia la izquierda a la lista de movimientos posibles
    if x < GRID_SIZE - 1:
        moves.append([x + 1, y]) # Agrega el movimiento hacia la derecha a la lista de movimientos posibles
    return moves # Devuelve la lista de movimientos posibles

# Por ejemplo en el primer if, si es posible moverse hacia arriba desde la posición actual, se agrega un nuevo movimiento a
# la lista moves. Este movimiento implica moverse una fila hacia arriba, manteniendo la misma columna. Por lo tanto, se crea
# una nueva coordenada [x, y - 1], donde y - 1 representa la fila anterior a la posición actual

def distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) # Calcula y devuelve la distancia Manhattan entre dos posiciones

# La función calcula la distancia entre dos puntos pos1 y pos2 utilizando la distancia de Manhattan.
# La distancia de Manhattan entre dos puntos en un plano es la suma de las diferencias absolutas de sus coordenadas horizontales y verticales.
# En este caso, abs(pos1[0] - pos2[0]) calcula la diferencia absoluta entre las coordenadas horizontales (columnas) de los puntos pos1 y pos2, y abs(pos1[1] - pos2[1]) calcula la diferencia absoluta entre las coordenadas verticales (filas) de los puntos pos1 y pos2.
# La suma de estas diferencias absolutas proporciona la distancia de Manhattan entre los dos puntos.

