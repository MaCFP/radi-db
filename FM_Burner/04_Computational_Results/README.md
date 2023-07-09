
# Information for Benchmarking
## General

### FDS - FM Burner 

#### Step by Step description to run a simulation with OpenFOAM
1. Download FDS template file 
2. Activate the configuration according to the relevant time step
3. Execute FDS with your usual command.
4. Post-Process: run `postFDS_FM.py` and `convertFM_FDS2CSV.py`

When you want to upload the data for comparison:
1. Adjust settings json/yaml file
2. Adjust README template for you simulatioin
3. Upload to github


### OPF - FM Burner
For comparison of OpenFOAM simulation results we provide an adapted fireFoam solver.
The differences are to the standard solver is basically just, that the adjusted solver just runs the radiation solver without momentum, pressure or energy equations.


#### Step by Step description to run a simulation with OpenFOAM
1. Create a new <folder>
2. Copy XXX data files to new <folder>
3. Setup radiation settings
4. Run `fireRadFoam`
5. Post-Process: 
   - `fireRadFoam -postProcess -fields "(qr)"` (if not activated before)
   - `postOPF_FM.py` and `convertFM_OPF2CSV.py`
6. Compare with benchmark

When you want to upload the data for comparison:
1. Adjust settings json/yaml file
2. Adjust README template for you simulatioin
3. Upload to github



# Information for post-processing


## General


### FDS - FM Burner - Post-Processing
### OPF - FM Burner - Post-Processing
