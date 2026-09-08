"""Grid 2D com obstáculos. Coordenadas em (linha, coluna), linha 0 no topo."""

import random


class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        # False = livre, True = obstáculo
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
        r, c = pos
        if allow_diagonal:
            deltas = [(-1, 0), (1, 0), (0, -1), (0, 1),
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]
        else:
            deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        result = []
        for dr, dc in deltas:
            npos = (r + dr, c + dc)
            if not self.in_bounds(npos) or self.is_wall(npos):
                continue

            if dr != 0 and dc != 0:
                # evita cortar o canto entre dois obstáculos
                if self.is_wall((r + dr, c)) or self.is_wall((r, c + dc)):
                    continue
                cost = 1.414213562
            else:
                cost = 1.0

            result.append((npos, cost))
        return result

    @staticmethod
    def random_grid(rows, cols, obstacle_ratio, start, goal, seed=None):
        """Grid aleatório; start e goal nunca ficam bloqueados."""
        rng = random.Random(seed)
        g = Grid(rows, cols)
        for r in range(rows):
            for c in range(cols):
                if (r, c) in (start, goal):
                    continue
                if rng.random() < obstacle_ratio:
                    g.set_wall((r, c))
        return g
