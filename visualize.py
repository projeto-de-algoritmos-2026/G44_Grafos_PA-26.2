import matplotlib.pyplot as plt
import matplotlib.patches as patches


def draw_grid(grid, start, goal, result, filename="astar_result.png"):
    fig, ax = plt.subplots(figsize=(8, 8))

    for r in range(grid.rows):
        for c in range(grid.cols):
            color = "#2b2d42" if grid.is_wall((r, c)) else "#f1f3f5"
            rect = patches.Rectangle((c, grid.rows - 1 - r), 1, 1,
                                      facecolor=color, edgecolor="#ced4da", linewidth=0.5)
            ax.add_patch(rect)

    # nós explorados que não fazem parte do caminho final
    path_set = set(result["path"]) if result["path"] else set()
    for (r, c) in result["visited_order"]:
        if (r, c) not in path_set:
            rect = patches.Rectangle((c, grid.rows - 1 - r), 1, 1,
                                      facecolor="#a5d8ff", edgecolor="#ced4da", linewidth=0.5)
            ax.add_patch(rect)

    if result["path"]:
        for (r, c) in result["path"]:
            rect = patches.Rectangle((c, grid.rows - 1 - r), 1, 1,
                                      facecolor="#51cf66", edgecolor="#ced4da", linewidth=0.5)
            ax.add_patch(rect)

    # start e goal ficam por cima
    sr, sc = start
    gr, gc = goal
    ax.add_patch(patches.Rectangle((sc, grid.rows - 1 - sr), 1, 1,
                                    facecolor="#339af0", edgecolor="black", linewidth=1.5))
    ax.text(sc + 0.5, grid.rows - 1 - sr + 0.5, "S", ha="center", va="center",
            fontsize=13, fontweight="bold", color="white")

    ax.add_patch(patches.Rectangle((gc, grid.rows - 1 - gr), 1, 1,
                                    facecolor="#f03e3e", edgecolor="black", linewidth=1.5))
    ax.text(gc + 0.5, grid.rows - 1 - gr + 0.5, "G", ha="center", va="center",
            fontsize=13, fontweight="bold", color="white")

    ax.set_xlim(0, grid.cols)
    ax.set_ylim(0, grid.rows)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])

    legend_elements = [
        patches.Patch(facecolor="#2b2d42", label="Obstáculo"),
        patches.Patch(facecolor="#a5d8ff", label="Explorado pelo A*"),
        patches.Patch(facecolor="#51cf66", label="Caminho final"),
        patches.Patch(facecolor="#339af0", label="Início (S)"),
        patches.Patch(facecolor="#f03e3e", label="Destino (G)"),
    ]
    ax.legend(handles=legend_elements, loc="upper center",
              bbox_to_anchor=(0.5, -0.02), ncol=3, fontsize=9)

    title = f"A* Pathfinding — {grid.rows}x{grid.cols}"
    if result["path"]:
        title += f"\nCusto do caminho: {result['cost']:.2f} | Nós explorados: {result['visited_count']}"
    else:
        title += "\nNenhum caminho encontrado!"
    ax.set_title(title, fontsize=12)

    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches="tight")
    plt.close()
    return filename
