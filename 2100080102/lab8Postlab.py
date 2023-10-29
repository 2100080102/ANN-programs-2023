import numpy as np
# Define the training data and targets
X = np.array([[1, 1, 1, 1],
              [-1, 1, -1, -1],
              [1, 1, 1, -1],
              [1, -1, -1, 1]])
t= np.array([1, 1, -1, -1])
# Initialize weights to 0
w= np.zeros(X.shape[1])
# Learning rate
learningrate = 1
# Number of iterations
maxiterations = 1000
# Perceptron learning algorithm
for iteration in range(maxiterations):
    errorcount = 0
    for i in range(len(X)):
        x = X[i]
        target = t[i]
        predicted = np.dot(x, w)
        if predicted * target <= 0:
            w += learningrate * target * x
            errorcount += 1
    if errorcount == 0:
        print(f"Converged after {iteration + 1} iterations.")
        break
# Print the learned weights
print("Learned weights:", w)
