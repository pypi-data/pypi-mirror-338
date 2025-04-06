# nep
**Description:**  
Trains potential functions using NEP.
## Input Parameters

**Usage:**  
```bash
NepTrain nep [options]
```

**Options:**  
- `-dir, --directory`  
  Path for NEP calculations. Default: `./cache/nep`.
- `-in, --in`  
  Path to `nep.in` file. Default: `./nep.in`.
- `-train, --train`  
  Path to `train.xyz` file. Default: `./train.xyz`.
- `-test, --test`  
  Path to `test.xyz` file. Default: `./test.xyz`.
- `-nep, --nep`  
  Path to potential function file. Default: `./nep.txt`.
- `-pred, --prediction`  
  Enable prediction mode. Default: `False`.
- `-restart, --restart_file`  
  Path to restart file. Default: `None`.
- `-cs, --continue_step`  
  Steps to continue from restart. Default: `10000`.
## Output

 