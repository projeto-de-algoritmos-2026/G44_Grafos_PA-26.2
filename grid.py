"""
grid.py
-------
Representação de um grid 2D (labirinto) com obstáculos, usado como
"mapa" para o algoritmo A*.

Convenção de coordenadas: (linha, coluna), linha 0 no topo.
"""

import random


class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        # matriz de células: False = livre, True = obstáculo
        self.walls = [[False] * cols for _ in range(rows)]

    def in_bounds(self, pos):
        r, c = pos
        return 0 <= r < self.rows and 0 <= c < self.cols

    def is_wall(self, pos):
        r, c = pos
        return self.walls[r][c]

    def set_wall(self, pos):
        r, c = pos
        self.walls[r][c] = True

    def neighbors(self, pos, allow_diagonal=False):
        """
        Retorna os vizinhos válidos (dentro do grid e sem obstáculo).
        Por padrão só move nas 4 direções (cima/baixo/esquerda/direita),
        que é a convenção mais simples e mais fácil de explicar/defender.
        """
        r, c = pos
        if allow_diagonal:
            deltas = [(-1, 0), (1, 0), (0, -1), (0, 1),
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]
        else:
            deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        result = []
        for dr, dc in deltas:
            npos = (r + dr, c + dc)
            if self.in_bounds(npos) and not self.is_wall(npos):
                # custo da diagonal é sqrt(2), do movimento reto é 1
                cost = 1.414213562 if (dr != 0 and dc != 0) else 1.0
                result.append((npos, cost))
        return result

    @staticmethod
    def random_grid(rows, cols, obstacle_ratio, start, goal, seed=None):
        """
        Gera um grid aleatório com uma certa proporção de obstáculos,
        garantindo que start e goal nunca fiquem bloqueados.
        """
        rng = random.Random(seed)
        g = Grid(rows, cols)
        for r in range(rows):
            for c in range(cols):
                if (r, c) in (start, goal):
                    continue
                if rng.random() < obstacle_ratio:
                    g.set_wall((r, c))
        return g
