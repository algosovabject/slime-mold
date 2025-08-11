import matplotlib.pyplot as plt
import networkx as nx
import random
from collections import Counter
from oracle import weighted_pseudopod_walk


def simulate_exploration(G, start, num_walks=50, max_steps=6, backtrack_chance=0.3):
    edge_hits = Counter()
    for _ in range(num_walks):
        current = start
        prev = None
        for _ in range(max_steps):
            neighbors = list(G.successors(current))
            if not neighbors:
                break
            # Occasionally backtrack to simulate exploratory indecision
            if prev and random.random() < backtrack_chance:
                next_node = prev
            else:
                next_node = random.choice(neighbors)
            edge_hits[(current, next_node)] += 1
            prev, current = current, next_node
    return edge_hits


def plot_exploration_and_pruned(G, start, pruned_path, edge_hits, ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_facecolor("black")  # Set background to black
    fig.patch.set_facecolor("black")

    pos = nx.spring_layout(G, seed=42)

    # Draw all nodes in muted gray for non-active
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='dimgray', ax=ax)
    nx.draw_networkx_labels(
        G,
        pos,
        labels={n: G.nodes[n]['label'] for n in G.nodes},
        font_size=8,
        font_color='white',
        ax=ax
    )

    # Base edges (exploration intensity) → orange glow
    max_hits = max(edge_hits.values()) if edge_hits else 1
    for (u, v), hits in edge_hits.items():
        width = 1 + (4 * hits / max_hits)

        # Glow layers
        for glow_level in range(4, 0, -1):
            alpha = 0.02 + 0.1 * (glow_level / 4)
            glow_width = width + (glow_level * 2)
            ax.plot(
                [pos[u][0], pos[v][0]],
                [pos[u][1], pos[v][1]],
                linewidth=glow_width,
                color='orange',
                alpha=alpha,
                zorder=1
            )

        # Core orange edge
        ax.plot(
            [pos[u][0], pos[v][0]],
            [pos[u][1], pos[v][1]],
            linewidth=width,
            color='orange',
            alpha=0.6,
            zorder=2
        )

    # Pruned path (lime green glow)
    path_edges = list(zip(pruned_path, pruned_path[1:]))
    for glow_level in range(6, 0, -1):
        alpha = 0.03 + 0.15 * (glow_level / 6)
        width = 8 * (glow_level / 6)
        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=path_edges,
            width=width,
            edge_color='limegreen',
            alpha=alpha,
            ax=ax
        )

    # Core pruned path edge
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=path_edges,
        width=3,
        edge_color='limegreen',
        ax=ax
    )

    # Node glow for pruned path
    for glow_size, glow_alpha in [(900, 0.05), (700, 0.1), (500, 0.2)]:
        nx.draw_networkx_nodes(
            G,
            pos,
            nodelist=pruned_path,
            node_size=glow_size,
            node_color='limegreen',
            alpha=glow_alpha,
            ax=ax
        )

    # Core pruned nodes
    nx.draw_networkx_nodes(
        G,
        pos,
        nodelist=pruned_path,
        node_size=600,
        node_color='limegreen',
        ax=ax
    )

    ax.set_title("Exploration (orange) → Pruned Path (green)", color='white')
    ax.axis('off')
    return ax
