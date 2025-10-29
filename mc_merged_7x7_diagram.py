import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Define new merged transition matrix (7x7)
# Order of states: [1, A, 3, 4, 5, 6, 7]
P_merged = np.array([
    [0.1, 0.2, 0.3, 0,   0.1, 0.1, 0.2],  # From state 1
    [0.1, 0.5, 0.1, 0,   0.3, 0,   0],    # From A
    [0.2, 0.3, 0.2, 0.1, 0.1, 0,   0.1],  # From 3
    [0.3, 0.1, 0.1, 0.2, 0.1, 0.1, 0.1],  # From 4
    [0.2, 0.7, 0,   0,   0.1, 0,   0],    # From 5
    [0.2, 0.2, 0.1, 0,   0.3, 0.1, 0.1],  # From 6
    [0.1, 0.3, 0.2, 0,   0.2, 0,   0.2],  # From 7
])

states = ["1", "A", "3", "4", "5", "6", "7"]

# Create directed graph
G = nx.DiGraph()

# Add edges where probability > 0
for i, s_from in enumerate(states):
    for j, s_to in enumerate(states):
        p = P_merged[i, j]
        if p > 0:
            G.add_edge(s_from, s_to, weight=p, label=f"{p:.2f}")

# Define layout
pos = nx.spring_layout(G, seed=42)

# Draw nodes and edges
nx.draw_networkx_nodes(G, pos, node_color="#89CFF0", node_size=1000)
nx.draw_networkx_labels(G, pos, font_weight="bold")
nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=15, edge_color="gray")

# Add edge labels (transition probabilities)
edge_labels = nx.get_edge_attributes(G, "label")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

plt.title("Merged Markov Chain Diagram (States 2 & 8 → A)")
plt.axis("off")
plt.show()
