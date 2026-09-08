from grid import Grid
from astar import astar, manhattan, zero
from visualize import draw_grid


def main():
    rows, cols = 10, 10
    start = (0, 0)
    goal = (9, 9)

    # sem seed: labirinto diferente a cada execução
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

        # mesmo grid e mesmo código, só com h(n) = 0
        dijkstra = astar(grid, start, goal, heuristic=zero, allow_diagonal=False)

        print("\n" + "-" * 60)
        print("Comparação A* x Dijkstra")
        print("-" * 60)
        print(f"A*:       {result['visited_count']:3d} nós expandidos   custo {result['cost']:.2f}")
        print(f"Dijkstra: {dijkstra['visited_count']:3d} nós expandidos   custo {dijkstra['cost']:.2f}")

        economia = dijkstra["visited_count"] - result["visited_count"]
        reducao = 100 * economia / dijkstra["visited_count"]
        print(f"\nA heurística de Manhattan evitou {economia} expansões ({reducao:.1f}% a menos),")
        print("chegando ao mesmo caminho de custo ótimo.")
    else:
        print("\nNenhum caminho encontrado entre início e destino!")

    filename = draw_grid(grid, start, goal, result, "astar_result.png")
    print(f"\nImagem salva em: {filename}")


if __name__ == "__main__":
    main()
