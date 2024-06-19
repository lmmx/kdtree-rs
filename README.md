# kdtree-rs

Test file:

- `dev_vectors.npy` with shape: [750000, 16]

Rust: `cargo run --release`

- Loaded npy file in 0.09s
- Built kd tree in 0.26s

Python: `python scipy_bench.py`

- Loaded npy file in 0.04 seconds
- Built KDTree in 0.95 seconds
