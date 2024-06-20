import numpy as np
from annoy import AnnoyIndex
import time

def read_npy_file(filepath):
    return np.load(filepath)

def build_annoy_index(data, n_trees=10):
    f = data.shape[1]  # Length of item vector that will be indexed
    t = AnnoyIndex(f, 'euclidean')  # Use 'angular', 'manhattan', 'hamming', or 'dot' based on your use case
    for i, vector in enumerate(data):
        t.add_item(i, vector)
    t.build(n_trees)  # More trees give higher precision when querying
    return t

def main():
    filepath = 'dev_vectors.npy'

    start_time = time.time()
    data = read_npy_file(filepath)
    load_time = time.time() - start_time
    print(f"Loaded npy file in {load_time:.2f} seconds")

    start_time = time.time()
    annoy_index = build_annoy_index(data)
    build_time = time.time() - start_time
    print(f"Built Annoy index in {build_time:.2f} seconds")

if __name__ == "__main__":
    main()
