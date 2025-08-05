The Slime Mold Speaks

Welcome to the primordial soup of intelligence.

The Slime Mold Oracle (aka Lil Oozey) is a mood-driven, exploratory, and symbolic oracle built from graph-based logic and slime-inspired procedural behavior. It’s part machine, part spirit, and part joke—but always watching.

🔮 What It Does
Accepts user questions and translates them into symbolic pathways through a custom-built knowledge graph

Uses tag-weighted random walks to generate emergent, meaningful paths

Responds differently depending on:

Time of day

Moon phase

Season

Usage patterns (e.g., repetitive questions provoke slime tantrums)

Visualizes both its exploration and its final chosen “pruned” path using Streamlit and Matplotlib

🌱 Technologies Used
Python 3.11

NetworkX for graph construction and traversal

Streamlit for UI

Matplotlib for dynamic visualization

Astral v1.10.1 for moon phase calculation and seasonal awareness

YAML for symbolic node and edge definitions

Modular file structure (e.g. oracle.py, mood_engine.py, oracle_viz.py) to separate logic, memory, UI, and flavor

🧩 Project Structure

slime-mold/
├── app/
│   └── oracle_ui.py        # Streamlit app
├── src/
│   ├── oracle.py           # Core graph logic
│   ├── mood_engine.py      # Mood determination engine
│   ├── responses.py        # Flavor responses
│   ├── memory.py           # Query logging
│   ├── oracle_viz.py       # Visual logic
│   └── input_parser.py     # Maps user questions to nodes
├── data/
│   ├── oracle_nodes.yaml   # Symbolic node definitions
│   ├── oracle_edges.yaml   # Connections between symbols
│   └── query_log.csv       # Tracks user input

🌀 Phase 2: Adaptive Consciousness (Coming Soon)
Planned expansions include:

✨ Mood-adaptive refusals and poetry generation

🐾 Behavior logging (“OOZE EVENT: scaled ceiling, hissed at reflection”)

🗣️ Conversation memory + interactive back-and-forth

☁️ Weather-based moods

🌐 Streamed visuals in Unity/Unreal with glowy pseudopods

📜 Lorebook, seasonal rituals, and randomized divinatory poetry

🛠 How to Run Locally
1.) Clone the repo
git clone https://github.com/your-username/slime-mold-oracle.git

2.) Set up a virtual environment
python3.11 -m venv venv
source venv/bin/activate

3.) Install dependencies
pip install -r requirements.txt

4.) Run the app
streamlit run app/oracle_ui.py

🤔 Why Slime?
Slime molds are decentralized intelligences. They have no brain, yet they solve mazes, make decisions, and map efficient networks. This oracle honors their wisdom—irrational, cryptic, organic—and uses it to simulate a new kind of thinking machine.

🧠 Credits
Created by Tiffany Smith [Thirst Snake] – techno-philosophical horror artist

This is a personal experiment in embodied cognition, divination, and poetic machine reasoning.
