use std::time::Instant;
use kiddo::KdTree;
use std::env;
use std::path::Path;
use npyz::NpyFile;

fn get_vector_path() -> Result<String, String> {
    let exe_path = env::current_exe().unwrap();
    let exe_dir = exe_path.parent().unwrap();
    let grandparent_dir = exe_dir
        .ancestors()
        .nth(2)
        .unwrap();
    let file_path = Path::new(grandparent_dir).join("dev_vectors.npy");
    println!("Vector file for src/main.rs: {:?}", file_path);
    Ok(file_path.to_str().expect("File path not str coercible").to_string())
}

fn read_npy_file() -> (Vec<f64>, u64) {
    let file_path = get_vector_path().unwrap();
    let reader = std::io::BufReader::new(std::fs::File::open(&file_path).unwrap());
    let npy = NpyFile::new(reader).unwrap();
    let shape = npy.shape();
    println!("npy loaded with shape: {:?}", shape);
    let _n = shape[0]; // number of samples
    let m = shape[1]; // vector dimension
    (npy.into_vec().unwrap(), m)
}

fn main() {
    let start = Instant::now();
    let (data, _dimension) = read_npy_file();
    println!("Loaded npy file in {:.2?}s", start.elapsed().as_secs_f64());
    let start = Instant::now();
    let _kdtree = build_16d_kdtree(data);
    println!("Built kd tree in {:.2?}s", start.elapsed().as_secs_f64());
}

fn build_16d_kdtree(data: Vec<f64>) -> KdTree<f64, 16> {
    let dimension = 16;
    let num_samples = data.len() / dimension;
    let mut points = Vec::with_capacity(num_samples);

    for i in 0..num_samples {
        let start = i * dimension;
        let end = start + dimension;
        let point = data[start..end].to_vec();
        points.push(point);
    }

    KdTree::new()
}
