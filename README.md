# kdtree-rs

## Result

Rust version with npyz/kiddo is 3x faster than numpy/scipy in Python

## Benchmarking

### 750k 16D vectors

Test file:

- `dev_vectors.npy` with shape: [750000, 16]

Rust: `cargo run --release`

- Loaded npy file in 0.09s
- Built kd tree in 0.32s

Python: `python scipy_bench.py`

- Loaded npy file in 0.04 seconds
- Built KDTree in 0.95 seconds

### 5M 16D vectors

Rust:

- Loaded npy file in 0.43s
- Built kd tree in 2.18s

Python:

- Loaded npy file in 0.25 seconds
- Built KDTree in 6.00 seconds

### 1M 100D vectors

Rust:

- Loaded npy file in 0.70s
- Built kd tree in 1.53s

Python:

- Loaded npy file in 0.31 seconds
- Built KDTree in 4.27 seconds
- Serialised KDTree in 1.63 seconds
- Reloaded KDTree in 0.20 seconds

### 5M 128D vectors

Rust:

- Loaded npy file in 6.10s
- Built kd tree in 8.26s

Python:

- Loaded npy file in 2.51 seconds
- Built KDTree in 20.15 seconds
