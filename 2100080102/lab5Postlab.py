import numpy as np

# Define input vector X (example data)
X = np.array([0.5, 0.3, 0.7])

# Define weight matrix W (example weights)
W = np.array([[0.2, 0.3, -0.1],
              [-0.5, 0.7, 0.4],
              [0.1, -0.2, 0.6]])

# Define bias vector b (example biases)
b = np.array([0.1, -0.3, 0.2])

# Define activation function (e.g., sigmoid)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Calculate activations of hidden layer (Z)
Z = np.dot(W, X) + b
a = sigmoid(Z)

print("Activations of the hidden layer:")
print(a)

# Define threshold values for activation
thresholds = np.array([0.5, 0.6, 0.7])

# Check if neurons are activated based on thresholds
activated_neurons = a > thresholds
print("Activated neurons:")
print(activated_neurons)
