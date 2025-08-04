import yaml
import networkx as nx
import random

def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def load_oracle_graph(nodes_path, edges_path):
    node_data = load_yaml(nodes_path)
    edge_data = load_yaml(edges_path)

    G = nx.DiGraph()

    for node in node_data['nodes']:
        G.add_node(
            node['id'],
            label=node.get('label', ''),
            meaning=node.get('meaning', ''),
            tags=node.get('tags', [])
        )

    for edge in edge_data['edges']:
        G.add_edge(
            edge['source'],
            edge['target'],
            weight=edge.get('weight', 1)
        )

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

def print_oracle_path(G, path):
    print("\nYour path through the Oracle of Ooze:")
    for node in path:
        label = G.nodes[node].get('label', node)
        meaning = G.nodes[node].get('meaning', '')
        print(f"> {label}: {meaning}")

# Quick script runner
if __name__ == "__main__":
    G = load_oracle_graph(
        "/Users/thirstsnake/Documents/Projects/slime-mold/data/oracle_nodes.yaml",
        "/Users/thirstsnake/Documents/Projects/slime-mold/data/oracle_edges.yaml"
    )
    path = walk_graph(G)
    print_oracle_path(G, path)
