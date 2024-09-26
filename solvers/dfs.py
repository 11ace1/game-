from game import get_neighbors

def dfs():
    start = (0, 0, 0, 0)  # Начальное состояние
    goal = (1, 1, 1, 1)   # Целевое состояние
    stack = [(start, [])]  # Стек (состояние, путь к нему)
    visited = set([start])  # Посещённые состояния

    while stack:
        current_state, path = stack.pop()
        if current_state == goal:
            return path + [goal]

        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [current_state]))

    return None  # Если решения нет