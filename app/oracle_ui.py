import sys
import os

# Add src/ to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import random
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import time

from oracle import load_oracle_graph, weighted_pseudopod_walk
from oracle_viz import simulate_exploration, plot_exploration_and_pruned
from mood_engine import get_oracle_mood
from input_parser import load_input_map, parse_input
from memory import log_query
from responses import get_flavor_line, get_season_flavor
from interpreter import interpret_path

st.set_page_config(page_title="The Great Lil Oozey", page_icon="🧠")
st.title("🧠 The Slime Mold Speaks")

# Load everything
G = load_oracle_graph("data/oracle_nodes.yaml", "data/oracle_edges.yaml")
input_map = load_input_map("data/input_map.yaml")
mood = get_oracle_mood()

selected_vibe = random.choice(mood['vibe'])

# Get a matching flavor line and season flavor, also single sentences
flavor_line = get_flavor_line(selected_vibe)
season_line = get_season_flavor(mood['season'])

# Compose a natural paragraph describing the mold’s mood
mood_description = f"{flavor_line} {season_line}"

st.markdown(mood_description)

user_input = st.text_input("What question will you lay at the slime mold's uh, feet?")

if user_input:
    start_node = parse_input(user_input, input_map)

    if start_node is None:
        st.warning("The ooze doesn't understand your question.")
    else:
        path = weighted_pseudopod_walk(G, start=start_node)
        matched_tags = G.nodes[start_node]['tags']
        log_query(user_input, path, matched_tags)

        # Prepare node data list for interpreter
        path_nodes = [G.nodes[n] for n in path]
        oracle_response = interpret_path(path_nodes)
        st.success("The ooze responds:")
        st.markdown(oracle_response)

        edge_hits = simulate_exploration(G, start_node, num_walks=40, max_steps=5)
        pruned_path = weighted_pseudopod_walk(G, start=start_node)
        fig, ax = plot_exploration_and_pruned(
        G, start_node, pruned_path, edge_hits, play_breathing_sound=True
        )
        st.pyplot(fig)


if user_input and start_node:
    pos = nx.spring_layout(G, seed=42)  # consistent layout
    node_colors = []

    for node in G.nodes:
        if node in path:
            node_colors.append("limegreen")
        else:
            node_colors.append("lightgray")
