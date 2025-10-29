import numpy as np

P = np.array([
    [0.1, 0,   0.1, 0.25, 0,   0.1, 0.25, 0.2],
    [0.1, 0.2, 0,   0,    0.3, 0,   0.1, 0.3],
    [0.1, 0.1, 0.1, 0.3,  0.1, 0,   0.1, 0.2],
    [0.25,0.1, 0.2, 0,    0.1, 0.1, 0.25,0],
    [0, 0.6, 0, 0.1, 0.1, 0.1, 0, 0.1],
    [0.2, 0.1, 0, 0.2, 0.2, 0.1, 0.1, 0.1],
    [0.3, 0.2, 0.1, 0.1, 0.1, 0.1, 0, 0.1],
    [0.1, 0.25, 0.1, 0, 0.3, 0, 0, 0.25]
])

# Solve πP = π -> (P.T - I)π = 0
A = P.T - np.eye(8)
# Add normalization condition
A = np.vstack([A, np.ones(8)])
b = np.zeros(9)
b[-1] = 1

pi = np.linalg.lstsq(A, b, rcond=None)[0]
pi = np.round(pi, 4)
print("Steady-state probabilities (π):")
print(pi)
