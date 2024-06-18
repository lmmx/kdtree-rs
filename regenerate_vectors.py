import numpy as np

# Generate a random float64 array of shape (750000, 16)
random_array = np.random.rand(750000, 16).astype(np.float64)

# Save the array as a .npy file
np.save('dev_vectors.npy', random_array)

print("Array saved as dev_vectors.npy")
