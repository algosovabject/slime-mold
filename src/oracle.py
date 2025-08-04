import yaml
import networkx as nx
import random  # Don't forget this import for walk_graph

def load_oracle_graph(yaml_path):
    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)

    G = nx.DiGraph()

    for node in data['nodes']:
        G.add_node(node['id'], label=node['label'], meaning=node['meaning'], tags=node['tags'])

    for edge in data['edges']:
        G.add_edge(edge['source'], edge['target'], weight=edge['weight'])

    return G

def walk_graph(G, start='life', steps=3):
    path = [start]
    current = start

    for _ in range(steps):
        neighbors = list(G.successors(current))
        if not neighbors:
            break
        current = random.choice(neighbors)
        path.append(current)

    return path

# Test run
if __name__ == "__main__":
    G = load_oracle_graph("oracle_nodes.yaml")
    path = walk_graph(G)
    print("Traversal path:", path)
