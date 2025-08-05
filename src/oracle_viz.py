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

    pos = nx.spring_layout(G, seed=42)

    # Draw all nodes lightly
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightgray', ax=ax)
    nx.draw_networkx_labels(G, pos, labels={n: G.nodes[n]['label'] for n in G.nodes}, font_size=8, ax=ax)

    # Base edges (exploration intensity)
    max_hits = max(edge_hits.values()) if edge_hits else 1
    for (u, v), hits in edge_hits.items():
        # Thickness proportional to exploration frequency
        width = 1 + (4 * hits / max_hits)
        ax.plot(
            [pos[u][0], pos[v][0]],
            [pos[u][1], pos[v][1]],
            linewidth=width,
            color='orange',
            alpha=0.4,
            zorder=1
        )
    # Draw pruned path on top
    path_edges = list(zip(pruned_path, pruned_path[1:]))

    # Edge glow: draw multiple increasingly thinner/lighter layers
    for glow_level in range(4, 0, -1):  # outer to inner
        alpha = 0.05 + 0.15 * (glow_level / 4)  # softer outside
        width = 8 * (glow_level / 4)
        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=path_edges,
            width=width,
            edge_color='limegreen',
            alpha=alpha,
            ax=ax,
            connectionstyle="arc3,rad=0.0"
        )
    # Core pruned path edge (brightest)
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=4, edge_color='limegreen', ax=ax)

    # Node glow: draw halos by drawing same nodes larger with low alpha underneath
    for glow_size, glow_alpha in [(900, 0.08), (600, 0.15), (400, 0.3)]:
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
    nx.draw_networkx_nodes(G, pos, nodelist=pruned_path, node_size=600, node_color='limegreen', ax=ax)

    fig, ax = plt.subplots(figsize=(8,6))
    plot_exploration_and_pruned(G, start_node, path, edge_hits, ax=ax)
    st.pyplot(fig)

    ax.set_title("Exploration (orange) → Pruned Path (green)")
    ax.axis('off')
    return ax