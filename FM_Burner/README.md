
# General Information

# Experimental data

The main directory for the FM-Burner is in the `macfp-db` project:
https://github.com/MaCFP/macfp-db/tree/master/Extinction/FM_Burner

There, the experimental setup for the `FM-Burner` is described in detail: 
https://github.com/MaCFP/macfp-db/tree/master/Extinction/FM_Burner/Documentation


And e.g. available experimental data is located at:
https://github.com/MaCFP/macfp-db/tree/master/Extinction/FM_Burner/Experimental_Data

# Scripts, Tools and Templates


## FDS
Template files:

| Case      | Name of template file |
|-----------|-----------------------|
| FM Burner | vFDS_FM_Burner.fds    |
| NIST Pool | vFDS_NIST_Pool.fds    |


## OpenFOAM
### fireRadFoam 

`fireRadFoam` is an adjusted fireFoam solver, which is based on
standard `fireFoam` (ESI v2212) and runs only the radiation part.


## Python
