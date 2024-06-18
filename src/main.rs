// use kiddo::KdTree;
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

fn read_npy_file() -> Vec<f64> {
    let file_path = get_vector_path().unwrap();
    let reader = std::io::BufReader::new(std::fs::File::open(&file_path).unwrap());
    let npy = NpyFile::new(reader).unwrap();
    let shape = npy.shape();
    println!("npy loaded with shape: {:?}", shape);
    npy.into_vec().unwrap()
}

fn main() {
    let _data = read_npy_file();
    // let kdtree = build_kdtree(data, dimensions);
}

// fn build_kdtree(data: Vec<Vec<f64>>, dimensions: usize) -> KdTree<f64, u32> {
//     let mut tree = KdTree::new_with_dimensions(dimensions);
//     for (i, point) in data.iter().enumerate() {
//         tree.add(point.as_slice(), i as u32).expect("Failed to add point to KD-tree");
//     }
//     tree
// }
