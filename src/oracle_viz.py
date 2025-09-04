import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random
import pygame
import time
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


def plot_exploration_and_pruned(G, start, pruned_path, edge_hits, ax=None, play_breathing_sound=False
):
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6))
    else:
        fig = ax.figure

    # Set black background for figure and axes
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")

    pos = nx.spring_layout(G, seed=42)

    # Draw all nodes lightly (gray)
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightgray', ax=ax)
    nx.draw_networkx_labels(
        G, pos,
        labels={n: G.nodes[n]['label'] for n in G.nodes},
        font_size=8,
        font_color='white',
        ax=ax
    )

    # Draw exploration edges in orange with thickness proportional to hits
    max_hits = max(edge_hits.values()) if edge_hits else 1
    for (u, v), hits in edge_hits.items():
        width = 1 + (4 * hits / max_hits)
        ax.plot(
            [pos[u][0], pos[v][0]],
            [pos[u][1], pos[v][1]],
            linewidth=width,
            color='orange',
            alpha=0.4,
            zorder=1
        )

    # Draw glowing pruned path edges in limegreen
    path_edges = list(zip(pruned_path, pruned_path[1:]))

    # Outer glows (multiple layers)
    for glow_level in range(4, 0, -1):
        alpha = 0.05 + 0.15 * (glow_level / 4)
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
    # Core pruned path edges (brightest)
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=4, edge_color='limegreen', ax=ax)

    # Node glow layers
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

    ax.set_title("Exploration (orange) → Pruned Path (green)", color='white')
    ax.axis('off')

    if play_breathing_sound:
        # Placeholder: insert your breathing sound code here,
        # e.g. trigger sound playback in separate thread or async
        pass

    return fig, ax


def pitch_shift(sound, semitones):
    """
    Pitch-shifts a pygame Sound by resampling it.
    Positive semitones shift pitch up, negative down.
    """
    arr = pygame.sndarray.array(sound)
    factor = 2 ** (semitones / 12.0)
    indices = np.round(np.arange(0, len(arr), factor)).astype(int)
    indices = indices[indices < len(arr)]
    shifted = arr[indices]
    shifted_sound = pygame.sndarray.make_sound(shifted)
    return shifted_sound


def plot_exploration_and_pruned_with_pitch_breathing(G, exploration_path, pruned_path, steps=40):
    pygame.mixer.init()
    try:
        pygame.mixer.music.load("ambient_drone.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(loops=-1)
    except Exception as e:
        print(f"[Audio] Ambient sound not loaded: {e}")

    try:
        click_sound = pygame.mixer.Sound("node_ping.wav")
        click_sound.set_volume(0.7)
    except Exception as e:
        print(f"[Audio] Click sound not loaded: {e}")
        click_sound = None

    try:
        base_breathe_sound = pygame.mixer.Sound("breath.wav")
        base_breathe_sound.set_volume(0.6)
    except Exception as e:
        print(f"[Audio] Breath sound not loaded: {e}")
        base_breathe_sound = None

    pos = nx.spring_layout(G, seed=42)
    fig, ax = plt.subplots(figsize=(8, 6), facecolor="black")
    ax.set_facecolor("black")

    for i in range(steps):
        ax.clear()
        ax.set_facecolor("black")

        nx.draw_networkx_nodes(G, pos, node_size=200, node_color="white", edgecolors="black")
        nx.draw_networkx_labels(G, pos, font_color="white")

        pulse_alpha = (np.sin(i / 2) + 1) / 2 * 0.7 + 0.3

        nx.draw_networkx_edges(
            G, pos,
            edgelist=exploration_path,
            edge_color=[(0, 1, 0, pulse_alpha)],
            width=2.5
        )

        nx.draw_networkx_edges(
            G, pos,
            edgelist=pruned_path,
            edge_color=[(1, 0.5, 0, pulse_alpha)],
            width=3
        )

        if click_sound and i % 5 == 0:
            click_sound.play()

        if base_breathe_sound and abs(pulse_alpha - 1.0) < 0.05:
            # Random semitone shift between -2 and +2 for subtle variation
            semitone_shift = np.random.uniform(-2, 2)
            shifted_breath = pitch_shift(base_breathe_sound, semitone_shift)
            shifted_breath.set_volume(0.6)
            shifted_breath.play()

        plt.pause(0.1)

    pygame.mixer.music.fadeout(1500)
    time.sleep(1)
    plt.show()