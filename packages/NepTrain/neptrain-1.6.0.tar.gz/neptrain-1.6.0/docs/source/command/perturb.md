# perturb
**Description:**  
Generates perturbed structures.
## Input Parameters

**Usage:**  
```bash
NepTrain perturb <model_path> [options]
```

**Options:**  
- `<model_path>`  
  The structure path or file for calculation (supports `xyz` and `vasp` formats).
- `-n, --num`  
  Number of perturbations for each structure. Default: `20`.
- `-c, --cell`  
  Deformation ratio. Default: `0.03`.
- `-d, --distance`  
  Minimum atom distance (Å). Default: `0.1`.
- `-o, --out`  
  Output file path for perturbed structures. Default: `./perturb.xyz`.
- `-a, --append`  
  Append to output file instead of overwriting. Default: `False`.
- `-f, --filter`  
  Filter structures based on minimum bond length. Default: `False`.
## Output