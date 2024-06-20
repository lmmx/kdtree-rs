import numpy as np

# Generate a random float64 array
random_array = np.random.rand(1000000, 128).astype(np.float64)

# Save the array as a .npy file
np.save('dev_vectors.npy', random_array)

print("Array saved as dev_vectors.npy")
