"""
main.py
-------
Gera um grid 10x10 com obstáculos, roda o A* do ponto de partida até o
destino, e salva a visualização do resultado.
"""

from grid import Grid
from astar import astar, manhattan
from visualize import draw_grid


def main():
    rows, cols = 10, 10
    start = (0, 0)
    goal = (9, 9)

    # grid aleatório com ~25% de obstáculos (sem seed = labirinto diferente a cada execução)
    grid = Grid.random_grid(rows, cols, obstacle_ratio=0.25,
                             start=start, goal=goal)

    print("=" * 60)
    print(f"A* Pathfinding em grid {rows}x{cols}")
    print(f"Início: {start}   Destino: {goal}")
    print("=" * 60)

    result = astar(grid, start, goal, heuristic=manhattan, allow_diagonal=False)

    if result["path"]:
        print(f"\nCaminho encontrado! Custo total: {result['cost']:.2f}")
        print(f"Tamanho do caminho: {len(result['path'])} células")
        print(f"Nós explorados pelo A*: {result['visited_count']} de {rows * cols} células totais")
        print(f"\nCaminho: {result['path']}")
    else:
        print("\nNenhum caminho encontrado entre início e destino!")

    filename = draw_grid(grid, start, goal, result, "astar_result.png")
    print(f"\nImagem salva em: {filename}")


if __name__ == "__main__":
    main()
