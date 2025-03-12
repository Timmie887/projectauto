import json

# Load the JSON file
with open("Ultimate_Personal_Assistant.json", "r") as file:
    data = json.load(file)

# Extract relevant information
agent_name = data.get("name", "Unknown Agent")
nodes = data.get("nodes", [])

# Display extracted details
print(f"🚀 Running {agent_name}")
print(f"🔹 Number of Nodes: {len(nodes)}")

# Example: Loop through nodes and print their names
for node in nodes:
    node_name = node.get("name", "Unnamed Node")
    print(f"➡ Processing Node: {node_name}")
