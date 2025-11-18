import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Options: 'a', 'b', 'c', 'd', 'e', 'f', 'stock'
key = 'a' 
# ---------------------------

matrices = {
    'a': np.array([[1, 0, 0], [0, 1, 0], [1/3, 1/3, 1/3]]),
    'b': np.array([[0, 0.5, 0.5], [1, 0, 0], [1, 0, 0]]),
    'c': np.array([[0, 1, 0], [0, 0, 1], [0.5, 0.5, 0]]),
    'd': np.array([[1, 0, 0], [0, 0.5, 0.5], [0, 0.5, 0.5]]),
    'e': np.array([[0.5, 0, 0.5, 0, 0], [1/3, 1/3, 1/3, 0, 0], 
                   [0.5, 0, 0.5, 0, 0], [0, 0, 0, 0.5, 0.5], [0, 0, 0, 0.5, 0.5]]),
    'f': np.array([[0, 0.5, 0.5, 0, 0, 0], [0, 0, 0, 1/3, 1/3, 1/3], 
                   [0, 0, 0, 1/3, 1/3, 1/3], [1, 0, 0, 0, 0, 0], 
                   [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0]]),
    'stock': np.array([[0.9, 0.075, 0.025], [0.15, 0.8, 0.05], [0.25, 0.25, 0.5]])
}

P = matrices[key]
n = P.shape[0]

if key == 'stock':
    P_steady = np.linalg.matrix_power(P, 100)
    print(f"Steady State (Iterative) for {key}: {P_steady[0]}")

# Graph Plotting
states = [f"s{i+1}" for i in range(n)]
G = nx.DiGraph()
threshold = 0.01

for i in range(n):
    for j in range(n):
        if P[i, j] > threshold:
            G.add_edge(states[i], states[j], weight=P[i, j])

pos = nx.circular_layout(G) 

plt.figure(figsize=(8, 6))
nx.draw_networkx_nodes(G, pos, node_color="lightgreen", node_size=1500, edgecolors="black")
nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold")
nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=25, width=2, alpha=0.6, connectionstyle='arc3, rad = 0.1')

edge_labels = {(u, v): f"{d['weight']:.2f}" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, label_pos=0.3)

plt.title(f"Markov Chain: Problem ({key})", fontsize=14, fontweight="bold")
plt.axis("off")
plt.tight_layout()
plt.show()