import sys
import os

# Add src/ to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import random
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

from oracle import load_oracle_graph, weighted_pseudopod_walk
from mood_engine import get_oracle_mood
from input_parser import load_input_map, parse_input
from memory import log_query
from responses import get_flavor_line, get_season_flavor

st.set_page_config(page_title="Lil Oozey's Oracle", page_icon="🧠")
st.title("🧠 The Slime Mold Oracle")

# Load everything
G = load_oracle_graph("data/oracle_nodes.yaml", "data/oracle_edges.yaml")
input_map = load_input_map("data/input_map.yaml")
mood = get_oracle_mood()

st.subheader("Mood")
st.markdown(f"**Vibe:** {mood['vibe']}")
st.markdown(f"> {get_flavor_line(mood['usage'])}")
st.markdown(f"> {get_season_flavor(mood['season'])}")

user_input = st.text_input("What would you like to ask the Oracle?")

if user_input:
    start_node = parse_input(user_input, input_map)

    if start_node is None:
        st.warning("The ooze doesn't understand your question.")
    else:
        path = weighted_pseudopod_walk(G, start=start_node)
        matched_tags = G.nodes[start_node]['tags']
        log_query(user_input, path, matched_tags)

        st.success("The ooze responds:")
        for node in path:
            st.markdown(f"**{G.nodes[node]['label']}**: {G.nodes[node]['meaning']}")

if user_input and start_node:
    pos = nx.spring_layout(G, seed=42)  # consistent layout
    node_colors = []

    for node in G.nodes:
        if node in path:
            node_colors.append("limegreen")
        else:
            node_colors.append("lightgray")

    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=False, node_color=node_colors, node_size=400, edge_color='gray', alpha=0.5)
    nx.draw_networkx_labels(G, pos, labels={n: G.nodes[n]['label'] for n in G.nodes}, font_size=8)

    st.pyplot(plt)
