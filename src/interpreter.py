import yaml
import random

def load_riddles(file_path="riddle_pool.yaml"):
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def interpret_path(path_nodes, riddle_file="riddle_pool.yaml"):
    riddles = load_riddles(riddle_file)
    
    # Gather all tags from the path's nodes
    path_tags = set()
    for node in path_nodes:
        if "tags" in node:
            path_tags.update(node["tags"])
    
    # Find riddles whose tags intersect with the path tags
    matching_riddles = []
    for entry in riddles:
        if path_tags.intersection(set(entry.get("tags", []))):
            matching_riddles.extend(entry.get("riddles", []))
    
    if matching_riddles:
        return random.choice(matching_riddles)
    else:
        return "The mold whispers, but you do not yet understand..."