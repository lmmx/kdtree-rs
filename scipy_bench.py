import numpy as np
from scipy.spatial import KDTree
import time

def read_npy_file(filepath):
    return np.load(filepath)

def build_kdtree(data):
    return KDTree(data)

def main():
    filepath = 'dev_vectors.npy'

    start_time = time.time()
    data = read_npy_file(filepath)
    load_time = time.time() - start_time
    print(f"Loaded npy file in {load_time:.2f} seconds")

    start_time = time.time()
    kdtree = build_kdtree(data)
    build_time = time.time() - start_time
    print(f"Built KDTree in {build_time:.2f} seconds")

if __name__ == "__main__":
    main()
