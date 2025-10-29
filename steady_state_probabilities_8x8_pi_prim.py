import numpy as np

P_merged = np.array([
    [0.1, 0.2, 0.3, 0,   0.1, 0.1, 0.2],  # From state 1
    [0.1, 0.5, 0.1, 0,   0.3, 0,   0],    # From A
    [0.2, 0.3, 0.2, 0.1, 0.1, 0,   0.1],  # From 3
    [0.3, 0.1, 0.1, 0.2, 0.1, 0.1, 0.1],  # From 4
    [0.2, 0.7, 0,   0,   0.1, 0,   0],    # From 5
    [0.2, 0.2, 0.1, 0,   0.3, 0.1, 0.1],  # From 6
    [0.1, 0.3, 0.2, 0,   0.2, 0,   0.2],  # From 7
])
# Solve πP = π -> (P.T - I)π = 0
A = P_merged.T - np.eye(7)
# Add normalization condition
A = np.vstack([A, np.ones(7)])
b = np.zeros(8)
b[-1] = 1

pi = np.linalg.lstsq(A, b, rcond=None)[0]
pi = np.round(pi, 4)
print("Merged-Steady-state probabilities (π'):")
print(pi)
