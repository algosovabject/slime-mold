from graph_builder import load_graph
from ooze_engine import find_ooze_path

def main():
    G = load_graph('data/symbols.yaml')

    print("🔮 Welcome to the Oracle of Ooze 🔮")
    start = input("Enter starting symbol (e.g., 'hunger'): ").strip().lower()
    end = input("Enter ending symbol (e.g., 'rebirth'): ").strip().lower()

    path = find_ooze_path(G, start, end)

    if not path:
        print("☠️ The mold finds no path. Your question echoes unanswered.")
        return

    print("\n🧠 The mold has spoken:")
    for node in path:
        label = G.nodes[node]['label']
        meaning = G.nodes[node]['meaning']
        print(f"→ {label.upper()}: {meaning}")

if __name__ == "__main__":
    main()
