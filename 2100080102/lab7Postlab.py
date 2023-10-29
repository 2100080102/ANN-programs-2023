import numpy as np
# Define input patterns
x1 = np.array([1.0, -2, 1.5, 0.0])
x2 = np.array([1.0, -0.5, -2.0, -1.5])
x3 = np.array([0.0, 1.0, -1.0, 1.5])
x4 = np.array([1.0, 1.5, -1.75, -0.5])
inp = np.array([x1, x2, x3, x4])
# Initialize weights with zeros
w = np.array([0, 0, 0, 0], dtype=np.int32)
w1 = np.array([0, 0, 0, 0], dtype=np.int32)

# Define target values for each pattern
t = np.array([1, 1, 1, 1])
print('The modified values in weight and weight1:')
for i in range(len(inp)):
    w= w.astype(np.float64)
    w1 = w1.astype(np.float64)
    w += t[i] * inp[i]
    w1 += t[i] * inp[i]
    print('Weight:', w)
    print('Weight1:', w1)
