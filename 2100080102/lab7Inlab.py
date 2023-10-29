import numpy as np
# Define input patterns
x1 = np.array([1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1])
x2 = np.array([1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1, 1, 1])
# Create a 2D array 'inp' to hold the input patterns
inp = np.array([x1, x2])
# Print the input patterns
print("Input Patterns:")
print(inp)
# Initialize weights with zeros
w = np.zeros(len(x1))
# Define target values for each pattern
t = np.array([1, -1])
# Update weights using the Hebbian learning rule
print('\nThe modified values in inp:')
for i in range(0, len(inp)):
    c = inp[i] * t[i]
    w = w + c
# Print the updated weights
print("\nUpdated Weight:")
print(w)
