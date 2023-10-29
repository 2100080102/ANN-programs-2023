def mcculloch_pitts_andnot(x1, x2):
    # Assign weights
    w1 = 1  # Weight for X1
    w2 = -1  # Weight for X2
    # Set the threshold
    threshold = 0
    # Calculate the weighted sum
    weighted_sum = w1 * x1 + w2 * x2
    # Apply the threshold logic
    if weightedsum >= threshold:
        return 1
    else:
        return 0
# Test cases
print("ANDNOT Truth Table:")
print("X1 X2 Y")
print("0 0 ", mcculloch_pitts_andnot(0, 0))
print("0 1 ", mcculloch_pitts_andnot(0, 1))
print("1 0 ", mcculloch_pitts_andnot(1, 0))
print("1 1 ", mcculloch_pitts_andnot(1, 1))
