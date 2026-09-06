"""
astar.py
--------
Implementação do algoritmo A* para encontrar o caminho mais curto
entre dois pontos em um grid com obstáculos.

A* é uma extensão do Dijkstra: em vez de priorizar só o custo acumulado
g(n), ele prioriza f(n) = g(n) + h(n), onde h(n) é uma heurística que
estima a distância até o destino. Isso guia a busca "na direção certa"
e evita explorar nós que claramente não levam a lugar nenhum.
"""

import heapq


def manhattan(a, b):
    """Heurística de distância Manhattan (válida para movimento em 4 direções)."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def euclidean(a, b):
    """Heurística de distância Euclidiana (válida também com diagonais)."""
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def astar(grid, start, goal, heuristic=manhattan, allow_diagonal=False):
    """
    Executa o A* no grid, do ponto start até o ponto goal.

    Retorna um dicionário com:
        path            -> lista de posições do caminho encontrado (ou None se não existe)
        cost             -> custo total do caminho
        visited_order    -> ordem em que os nós foram definitivamente expandidos
        visited_count    -> quantos nós foram expandidos (métrica de eficiência)
    """
    # fila de prioridade: (f_score, contador_de_desempate, posição)
    counter = 0
    open_heap = [(heuristic(start, goal), counter, start)]

    came_from = {}
    g_score = {start: 0.0}
    visited_order = []
    closed = set()

    while open_heap:
        _, _, current = heapq.heappop(open_heap)

        if current in closed:
            continue
        closed.add(current)
        visited_order.append(current)

        if current == goal:
            return {
                "path": _reconstruct_path(came_from, current),
                "cost": g_score[current],
                "visited_order": visited_order,
                "visited_count": len(visited_order),
            }

        for neighbor, move_cost in grid.neighbors(current, allow_diagonal):
            tentative_g = g_score[current] + move_cost
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                came_from[neighbor] = current
                counter += 1
                heapq.heappush(open_heap, (f_score, counter, neighbor))

    # fila esvaziou sem achar o destino -> não existe caminho
    return {
        "path": None,
        "cost": float("inf"),
        "visited_order": visited_order,
        "visited_count": len(visited_order),
    }


def _reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path
