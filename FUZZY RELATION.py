
# Program to calculate Max-Min Composition

import numpy as np

# Define fuzzy relation matrices
R = np.array([
    [0.2, 0.7, 0.5],
    [0.8, 0.4, 0.6]
])

S = np.array([
    [0.5, 0.9],
    [0.6, 0.3],
    [0.7, 0.8]
])

# Calculate Max-Min Composition
T = np.zeros((R.shape[0], S.shape[1]))

for i in range(R.shape[0]):
    for j in range(S.shape[1]):
        values = []

        for k in range(R.shape[1]):
            values.append(min(R[i][k], S[k][j]))

        T[i][j] = max(values)

# Display the result
print("Fuzzy Relation Matrix R:")
print(R)

print("\nFuzzy Relation Matrix S:")
print(S)

print("\nMax-Min Composition (R o S):")
print(T)
