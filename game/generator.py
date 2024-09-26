# Проверка на безопасность состояния
def is_safe(state):
    farmer, wolf, goat, cabbage = state
    # Волк и коза без фермера, коза и капуста без фермера — недопустимо
    if (wolf == goat != farmer) or (goat == cabbage != farmer):
        return False
    return True

# Генерация допустимых соседних состояний
def get_neighbors(state):
    farmer, wolf, goat, cabbage = state
    moves = [(1, 0, 0, 0), (1, 1, 0, 0), (1, 0, 1, 0), (1, 0, 0, 1)] if farmer == 0 else [(-1, 0, 0, 0), (-1, -1, 0, 0), (-1, 0, -1, 0), (-1, 0, 0, -1)]
    neighbors = []
    for move in moves:
        new_state = tuple(x + y for x, y in zip(state, move))
        if all(0 <= i <= 1 for i in new_state) and is_safe(new_state):
            neighbors.append(new_state)
    return neighbors