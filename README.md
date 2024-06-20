# kdtree-rs

## Result

Rust version with npyz/kiddo is 3x faster than numpy/scipy in Python

## Benchmarking

### 750k 16D vectors

Test file:

- `dev_vectors.npy` with shape: [750000, 16]

Rust: `cargo run --release`

- Loaded npy file in 0.09s
- Built kd tree in 0.26s

Python: `python scipy_bench.py`

- Loaded npy file in 0.04 seconds
- Built KDTree in 0.95 seconds

### 5M 16D vectors

Rust:

- Loaded npy file in 0.43s
- Built kd tree in 1.32s

Python:

- Loaded npy file in 0.25 seconds
- Built KDTree in 6.00 seconds

### 1M 100D vectors

Rust:

- Loaded npy file in 0.67s
- Built kd tree in 0.52s

Python:

- Loaded npy file in 1.86 seconds
- Built KDTree in 3.33 seconds (SciPy)
- Built Annoy index in 8.33 seconds (Annoy)
