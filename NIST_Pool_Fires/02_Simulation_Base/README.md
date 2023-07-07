
# Overview

For this case, there is no mapping involved. So the relevant folder is just called `OpenFOAM`.
This folder includes scripts to download the openFOAM data automatically from the release

`OpenFOAM_Snapshots`
  - all the mapped field files are available in a release with compressed openfoam files; please click here to download the relevant time steps.
  - Link to data files for the release with each snapshot:
  
https://github.com/MaCFP/radi-db/releases/tag/NIST_Pool_SimBase_v0.0.1

Please use the scripts in the current `OpenFOAM_Snapshots` folder for downloading all files automatically.

```00_download_files.sh```

With the other two scripts you have a starting point to prepare OpenFOAM cases to start the evaluation. There are at the moment two options:

```01_createCaseFolder_separate.sh```

```02_createCaseFolder_combined.sh```

