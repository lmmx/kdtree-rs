import pickle
import time

import numpy as np
from scipy.spatial import KDTree, cKDTree

# from sklearn.neighbors import BallTree


def read_npy_file(filepath):
    return np.load(filepath)


def build_kdtree(data):
    return KDTree(data)


def build_ckdtree(data):
    return cKDTree(data)


def build_ball_tree(data):
    return BallTree(data)


def main():
    filepath = "dev_vectors.npy"

    start_time = time.time()
    data = read_npy_file(filepath)
    load_time = time.time() - start_time
    print(f"Loaded vectors from npy in {load_time:.2f} seconds")

    start_time = time.time()
    with open("dev_vectors.pkl", "wb") as f:
        pickle.dump(data, f)
    save_time = time.time() - start_time
    print(f"Serialised vectors to pickle in {save_time:.2f} seconds")

    start_time = time.time()
    kdtree = build_kdtree(data)
    build_time = time.time() - start_time
    print(f"Built KDTree in {build_time:.2f} seconds")

    start_time = time.time()
    ckdtree = build_ckdtree(data)
    build_time = time.time() - start_time
    print(f"Built cKDTree in {build_time:.2f} seconds")

    start_time = time.time()
    with open("kdtree.pkl", "wb") as f:
        pickle.dump(kdtree, f)
    save_time = time.time() - start_time
    print(f"Serialised KDTree to pickle in {save_time:.2f} seconds")

    # start_time = time.time()
    # ball_tree = build_ball_tree(data)
    # build_time = time.time() - start_time
    # print(f"Built BallTree in {build_time:.2f} seconds")


def restore():
    start_time = time.time()
    with open("dev_vectors.pkl", "rb") as f:
        data = pickle.load(f)
    reload_time = time.time() - start_time
    print(f"Reloaded vectors from pickle in {reload_time:.2f} seconds")

    start_time = time.time()
    with open("kdtree.pkl", "rb") as f:
        tree = pickle.load(f)
    reload_time = time.time() - start_time
    print(f"Reloaded KDTree from pickle in {reload_time:.2f} seconds")


if __name__ == "__main__":
    main()
    restore()
