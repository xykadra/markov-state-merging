import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Normalized transition matrix (from your problem)
P = np.array([
    [0, 0.5, 0.5, 0, 0, 0],
    [0, 0, 0, 1/3, 1/3, 1/3],
    [0, 0, 0, 1/3, 1/3, 1/3],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0]
])
# Parameters
threshold = 0.1  # show edges with P(i,j) > threshold
n = P.shape[0]
states = [f"s{i+1}" for i in range(n)]

# Create directed graph
G = nx.DiGraph()

# Add edges with probabilities as weights
for i in range(n):
    for j in range(n):
        if P[i, j] > threshold:
            G.add_edge(states[i], states[j], weight=P[i, j])

# Layout (you can try 'circular' or 'kamada_kawai' as well)
pos = nx.spring_layout(G, seed=42)

# Draw nodes and edges
plt.figure(figsize=(10, 8))
nx.draw_networkx_nodes(G, pos, node_color="skyblue", node_size=1200, edgecolors="black")
nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

# Draw edges with arrows
nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=30, width=2, alpha=0.7)

# Edge labels with probabilities
edge_labels = {(u, v): f"{d['weight']:.2f}" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)

plt.title("Problem 1. (f)", fontsize=14, fontweight="bold")
plt.axis("off")
plt.tight_layout()
plt.show()
