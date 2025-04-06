# select
**Description:**  
Selects samples from trajectory files.
## Input Parameters

**Usage:**  
```bash
NepTrain select <trajectory_path> [options]
```

**Options:**  
- `<trajectory_path>`  
  Path to trajectory file (xyz format).
- `-base, --base`  
  Path to `base.xyz` for sampling. Default: `base`.
- `-nep, --nep`  
  Path to `nep.txt` file for descriptor extraction. Default: `./nep.txt`.
- `-max, --max_selected`  
  Maximum number of structures to select. Default: `20`.
- `-d, --min_distance`  
  Minimum bond length for farthest-point sampling. Default: `0.01`.
- `--pca, -pca`  
  Use PCA for decomposition.
- `--umap, -umap`  
  Use UMAP for decomposition.
- `-o, --out`  
  Output file for selected structures. Default: `./selected.xyz`.
- **SOAP Parameters:**  
  - `-r, --r_cut`  
    Cutoff for local region (Å). Default: `6`.
  - `-n, --n_max`  
    Number of radial basis functions. Default: `8`.
  - `-l, --l_max`  
    Maximum degree of spherical harmonics. Default: `6`.
## Output