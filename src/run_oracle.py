from oracle import load_oracle_graph, walk_graph
from input_parser import load_input_map, parse_input

if __name__ == "__main__":
    G = load_oracle_graph("data/oracle_nodes.yaml", "data/oracle_edges.yaml")
    input_map = load_input_map("data/input_map.yaml")

    user_input = input("Ask the Ooze Oracle your question: ")
    start_node = parse_input(user_input, input_map)

    if start_node is None:
        print("The oracle gurgles uncertainly... it does not understand.")
    else:
        path = walk_graph(G, start=start_node)
        print("Your path through the Oracle of Ooze:")
        for node in path:
            print(f"> {G.nodes[node]['label']}: {G.nodes[node]['meaning']}")
