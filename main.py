from solvers import dfs, bfs


solution_bfs = bfs()
if solution_bfs:
    print("Решение найдено BFS:")
    for step in solution_bfs:
        print(step)
else:
    print("Решение не найдено.")
    
solution_dfs = dfs()
if solution_dfs:
    print("Решение найдено DFS:")
    for step in solution_dfs:
        print(step)
else:
    print("Решение не найдено.")