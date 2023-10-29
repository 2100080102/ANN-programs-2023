import numpy as np
# Define the OR function
def OR(x1, x2):
    # Define the input vector
    X = np.array([x1, x2])
    # Define the weights and bias for the perceptron
    w = np.array([1, 1])  # Weights
    b = -0.5  # Bias
    # Calculate the aggregated input
    aggregatedinput = np.dot(X, w) + b
    # Apply the threshold (step) function
    if aggregatedinput > 0:
        return 1
    else:
        return 0
# Test the OR function with different inputs
print("OR(0, 0) =", OR(0, 0))
print("OR(0, 1) =", OR(0, 1))
print("OR(1, 0) =", OR(1, 0))
print("OR(1, 1) =", OR(1, 1))
