# radi-db

## Introduction
Measurement and Computation of Radiative Heat Transfer Phenomena Database

Welcome to the MaCFP database!

The central objective of the MaCFP working group is to target
fundamental progress in fire science and to advance predictive fire
modeling. The purpose of this database is to host high-quality
experimental data for the purpose of validating physics-based fire
models. The working group meets before the IAFSS conference currently
held every three years.


## Folder Overview
In general for the test cases both folder structures are prepared in a similar manner. There are mainly differences when for a certain case data or scripts are only provided for selected CFD tools (e.g. for the NIST pool fire there is up to now no FDS mapping).

The General structure looks like:
- 00_Documentation
  - General Information about the case
- 01_Experimental_Data
  - Reference and description of available experimental data
- 02_Simulation_Base
  - This folder includes the mapped data which can be used within OpenFOAM or FDS for benchmarking. The subfolders with the suffix `_mapped_Snapshots` provide the scripts to download, run and post-process radiation settings.
- 03_Simulation_LBL_PMC
  - This folder includes the benchmark data (downloadable via the provided scripts) based on the PMC-LBL solver.
- 04_Computational_Results
  - As for the gas phase subgroup, there the computational results of the participants are stored.
  - An initial folder is provided for guidance with a very basic setup for FDS and OpenFOAM.
- 05_Utilities
  - This folder might include additional scripts for handling certain cases individually.

## File names
File names for scripts, folders and configurations files have often a
prefix with a number. These number should help to guide through the
usage of the available data and to run the actual simulation with the
additional data available on github.

E.g. when looking at the already mentioned folder naming approach:
- 00_Documentation
- 01_Experimental_Data
- 02_Simulation_Base
- 03_Simulation_LBL_PMC
- 04_Computational_Results

There the idea is that you would start with the folder with the prefix `00_` to start getting information about the case; the corresponding next folder to work on would be starting with `01_` and so on.

Further, when going into `02_Simulation_Base/FDS_mapped_Snapshots` there are scripts with similar prefixes:
- 00_download_files.sh
- 01_extract_tar_files.sh
- 02_adjust_copy_FDS_template.py
- 03_run_FDS.py

For working with the data files and setup one would start with the file starting with `00_` and going step by step to the next scripts.

The actual details are described within each folder.

## Benchmark Cases

### NIST Pool Fires

<short description>

### FM Burner 
<short description>



## Scripts, Tools and Templates


### OpenFOAM
#### fireRadFoam 

`fireRadFoam_MaCFP` is an adjusted fireFoam solver, which is based on
standard `fireFoam` (ESI v2212) and runs only the radiation part.


### Python
The plotting is done with the same approach and `macfp.py` script like for the gas phase group.

Further scripts are provided within the test cases.
