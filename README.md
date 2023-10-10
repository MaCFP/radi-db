# radi-db

Measurement and Computation of Radiative Heat Transfer Phenomena Database

Welcome to the MaCFP database!

The central objective of the MaCFP working group is to target
fundamental progress in fire science and to advance predictive fire
modeling. The purpose of this database is to host high-quality
experimental data for the purpose of validating physics-based fire
models. The working group meets before the IAFSS conference currently
held every three years.


<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [radi-db](#radi-db)
    - [Introduction](#introduction)
    - [Folder Overview](#folder-overview)
    - [File names](#file-names)
    - [Benchmark Cases](#benchmark-cases)
    - [Scripts, Tools and Templates](#scripts-tools-and-templates)
        - [OpenFOAM](#openfoam)
            - [fireRadFoam ](#fireradfoam)
        - [Python](#python)

<!-- markdown-toc end -->


## Introduction

<XXXX A bit more infoXXX>


## Folder Overview
In general for the test cases both folder structures are prepared in a similar manner. There are mainly differences when for a certain case data or scripts are only provided for selected CFD tools (e.g. for the NIST pool fire there is up to now no FDS mapping).

The General structure looks like:
- 00_Documentation
  - General Information about the case
- 01_Experimental_Data
  - Reference and description of available experimental data
- 02_Simulation_Base
  - This folder includes the initial "base" simulation setup of FDS for the FM Burner case and the OpenFOAM setup for the NIST Pool fire.
- 03_Simulation_LBL_PMC
  - This folder includes the benchmark data (downloadable via the provided scripts) based on the PMC-LBL solver.
- 04_Computational_Results
  - As for the gas phase subgroup, there the computational results of the participants are stored.
  - This folder includes also two template folders
    - One folder provides a template for the calculation with mapped
      data for FDS and OpenFOAM; these data can be used for
      benchmarking against the LBL-PMC data. The subfolders with the
      suffix `_mapped_Snapshots` provide the scripts to download, run
      and post-process radiation settings.
    - The second folder provides guidance for post-processing the results of the new calculations with FDS and OpenFOAM.
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

Detailed description about the benchmark cases are provided in the READMEs of the corresponding subfolders.

- NIST Pool Fires [NIST Pool Folder](/NIST_Pool_Fires/README.md)

- FM Burner: [FM Burner Folder](/FM_Burner/README.md)

## Naming conventions for fields

### Field Names

| Field           | Type                     | Field name for OPF | Field name for FDS |
|-----------------|--------------------------|--------------------|--------------------|
| Nitrogen        | Mass fraction            | N2                 |                    |
| Oxygen          | Mass fraction            | O2                 |                    |
| Carbon dioxide  | Mass fraction            | CO2                |                    |
| Carbon monoxide | Mass fraction            | CO                 |                    |
| Ethylene        | Mass fraction            | C2H4               |                    |
| Water Vapor     | Mass fraction            | H2O                |                    |
| Soot            | Mass fraction            | Soot               |                    |
| Nitrogen        | Volume fraction          | N2_vol             |                    |
| Oxygen          | Volume fraction          | O2_vol             |                    |
| Carbon dioxide  | Volume fraction          | CO2_vol            |                    |
| Carbon monoxide | Volume fraction          | CO_vol             |                    |
| Ethylene        | Volume fraction          | C2H4_vol           |                    |
| Water Vapor     | Volume fraction          | H2O_vol            |                    |
| Soot            | Volume fraction          | Soot_vol           |                    |
| Soot            | Aerosol Volume fraction  | fvSoot             |                    |
| Density         | (warning: dimensionless) | rho                |                    |
| Temperature     | (Kelvin)                 |                    |                    |

Comment: Pressure is not available in this list as it is not mapped and as it has minor impact
on the final results (this was checked for time step 15).

## Scripts, Tools and Templates


### OpenFOAM
#### fireRadFoam 

`fireRadFoam_MaCFP` is an adjusted fireFoam solver, which is based on
standard `fireFoam` (ESI v2212) and runs only the radiation part.

The adjusted solver is located in [Utilities OpenFOAM folder](/Utilities/OpenFOAM/fireRADFoam_MaCFP) .


### Python
The plotting is done with the same approach and `macfp.py` script like for the gas phase group.

Further scripts are provided within the test cases.
