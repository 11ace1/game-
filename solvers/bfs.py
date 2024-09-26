from collections import deque
from game import get_neighbors

def bfs():
    start = (0, 0, 0, 0)  # Начальное состояние
    goal = (1, 1, 1, 1)   # Целевое состояние
    queue = deque([(start, [])])  # Очередь (состояние, путь к нему)
    visited = set([start])  # Посещённые состояния

    while queue:
        current_state, path = queue.popleft()
        if current_state == goal:
            return path + [goal]

        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [current_state]))

    return None  # Если решения нет