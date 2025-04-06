# init
**Description:**  
Initializes file templates for NepTrain.
## Input Parameters

**Usage:**  
```bash
NepTrain init [-f]
```

**Options:**  
- `-f, --force`  
  Force overwriting of generated templates. Default: `False`.

## Output
:::{tip}
These output files serve as inputs for the `train` command. Detailed modification instructions are provided in the [train](train.md) section.
::: 
- `job.yaml`  
  The configuration file for automatic training (`config_path`).  

- `run.in`  
  The template file for molecular dynamics (MD).  

- `structure/`  
  This folder must contain the structures required for active learning. Multiple structures can be included, and the file format should be either `.xyz` or `.vasp`.  

- `sub_gpu.sh`  
  A script file for submitting NEP and GPUMD tasks. <span style="color:red;">Modify the queue information based on your cluster setup.</span>  

- `sub_vasp.sh`  
  A script file for submitting VASP tasks. <span style="color:red;">Modify the queue information based on your cluster setup. </span> 
### 可选的模板文件 
- INCAR
用户可以通过`INCAR`文件指定单点能的计算细节。如果没有指定则使用默认的INCAR。默认INCAR细节详见[INCAR](./vasp.md#default-incar)
- nep.in
如果没有指定该文件，会根据训练集自动判断元素种类，生成最简的nep.in。如果需要修改训练超参数，请自行创建该文件。
最简的nep.in如下
  ```text
    generation     100000
    type     3 I Cs Pb
    ```
## 文件修改
