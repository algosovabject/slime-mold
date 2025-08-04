from oracle import load_oracle_graph, walk_graph

G = load_oracle_graph("oracle_nodes.yaml")
path = walk_graph(G)

print("\nYour path through the Oracle of Ooze:")
for node_id in path:
    node = G.nodes[node_id]
    print(f"> {node['label']}: {node['meaning']}")
