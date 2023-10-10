
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Description for validating FDS and OpenFOAM with the PMC-LBL solution](#description-for-validating-fds-and-openfoam-with-the-pmc-lbl-solution)
    - [Step by Step description to compare a `FDS` simulation](#step-by-step-description-to-compare-a-fds-simulation)
        - [1. Got to folder](#1-got-to-folder)
        - [2. Download Snapshots from Github releases](#2-download-snapshots-from-github-releases)
        - [3. Creating Case directories by extracting the tar files for each snapshot](#3-creating-case-directories-by-extracting-the-tar-files-for-each-snapshot)
        - [4. Distribute an adjusted `FDS` template file](#4-distribute-an-adjusted-fds-template-file)
        - [5. Run all cases](#5-run-all-cases)
        - [6. Post-Processing of all Snapshots ](#6-post-processing-of-all-snapshots)
        - [7. Compare with `PMC-LBL`](#7-compare-with-pmc-lbl)
    - [Step by Step description to compare an `OpenFOAM` simulation](#step-by-step-description-to-compare-an-openfoam-simulation)
        - [1. Got to folder](#1-got-to-folder-1)
        - [2. Download Snapshots from Github releases](#2-download-snapshots-from-github-releases-1)
        - [3. Creating Case directories for each time step   ](#3-creating-case-directories-for-each-time-step)
        - [4. Distribute an adjusted `controlDict`](#4-distribute-an-adjusted-controldict)
        - [5. Run all cases](#5-run-all-cases-1)
        - [6. Post-Processing of all Snapshots ](#6-post-processing-of-all-snapshots-1)
        - [7. Compare with `PMC-LBL`](#7-compare-with-pmc-lbl-1)
    - [Step by Step description to post-process the `PMC-LBL` results](#step-by-step-description-to-post-process-the-pmc-lbl-results)
        - [1. Got to folder](#1-got-to-folder-2)
        - [2. Download Snapshots-Results from Github releases](#2-download-snapshots-results-from-github-releases)
        - [3. Creating Case directories for each time step   ](#3-creating-case-directories-for-each-time-step-1)
        - [4. Distribute a run script for the post-processing](#4-distribute-a-run-script-for-the-post-processing)
        - [5. Post-Process all cases](#5-post-process-all-cases)
        - [6. Post-Processing of all Snapshots ](#6-post-processing-of-all-snapshots-2)
    - [Step by Step description compare `FDS` and `OpenFOAM` reuslts with `PMC-LBL` benchmark](#step-by-step-description-compare-fds-and-openfoam-reuslts-with-pmc-lbl-benchmark)

<!-- markdown-toc end -->


# Overview Folder Structure
## `FDS_mapped_Snapshots`:
- `CSVF` files approach for calculating the snapshots with FDS

The general steps are described already in the [Readme](/FM_Burner/README.md) ; please check there again for the details and a step by step description.


## `OPF_Mapped_Snapshots`
  - all the mapped field files are available in a release with compressed openfoam files; please click here to download the relevant time steps.
  - Link to data files for the release with each snapshot:
  
  https://github.com/MaCFP/radi-db/releases/tag/FM_SimBase_v0.0.1

Please use the scripts in the current `OpenFOAM_mapped_Snapshots` folder for downloading all files automatically.

```00_download_files.sh```

The general steps are described already in the [Readme](/FM_Burner/README.md) ; please check there again for the details and a step by step description.



# Description for validating FDS and OpenFOAM with the PMC-LBL solution
It is assumed that a basic understanding about the FDS and OpenFOAM setup is already available for further descriptions.

These two description do not yet described how to compare the final results. This is done within the [04_Computational_Results](/FM_Burner/04_Computational_Results) folder. There the actual comparison of the results is done; this is very similar to the gas phase group.

## Step by Step description to compare a `FDS` simulation


### 1. Got to folder
   `/02_Simulation_Base/OpenFOAM_mapped_Snapshots`
   
   This is the link to the [folder](/FM_Burner/02_Simulation_Base/FDS_mapped_Snapshots).

   There you find scripts and some folders. 
   The main file which is needed is the template fds file [v0_FM_15cm_Burner_C2H4_20p9_5mm.fds](/FM_Burner/02_Simulation_Base/FDS_mapped_Snapshots/v0_FM_15cm_Burner_C2H4_20p9_5mm.fds).
   
   This file will be needed for the simulation of each snapshot.



### 2. Download Snapshots from Github releases

   The actual data for each snapshot is available within different github releases. The can be dowloaded manually or by exeecuting the script:

   `bash 00_download_files.sh`
   
   This script creates a directory called `Release` and will download the snapshots into this folder.
   
   

### 3. Creating Case directories by extracting the tar files for each snapshot
  
   These downloaded tar-files are extracted within the `Release`
   folder in separate directories.

   These newly created time folder include the initial conditions for
   each snapshot; the information is provided via `csv` files for each
   time step and each mesh (in total 64 meshes) for the relevant
   species and temperature.  
   
   `bash 01_extract_tar_files.sh`
  

### 4. Distribute an adjusted `FDS` template file

   Once a case snapshot structure is created, the `FDS` template file
   `v0_FM_15cm_Burner_C2H4_20p9_5mm.fds` will be copied to these
   directories with an adjustment of the CSVF section by typing:
   
   `python 02_adjust_copy_FDS_template.py`


### 5. Run all cases

   The next step is to run all snapshots with
 
   `python 03_run_FDS.py`
 
   By default, the script assumes, that your `FDS` installation is
   accessable (in your `PATH`) with the name `fds`; if this is not the
   case try to run the simulation via:
 
   `python 03_run_FDS.py <path_to_fds_bin/fds_something`
 
   Obviously, the settings within the
   `v0_FM_15cm_Burner_C2H4_20p9_5mm.fds` file can be adjusted as it
   is needed before the simulation. Though keep in mind that the
   defined devices are set and named like this to be able to compare
   results with the other OpenFOAM results.

   The primary ideas is to be able to adjust special radiation solver
   settings and evaluate its impact for each snapshot.


### 6. Post-Processing of all Snapshots 

   To run the post-processing for all snapshots, go into the `POST`
   directory
   
   `cd POST`
   
   and
   
   execute the python script
   
   `python 00_post_Extract_Data_and_Plot_Line_FDS.py`

   This script will do the actual post-processing of the
   calculations. It is prepared in a way to have similar name
   structure like for the other setups for `OpenFOAM` and for
   `PMC-LBL`.

   Two directories, one with the name `LinePlots` and the other one
   with the name `DataFiles` are created.
   
   `LinePlots`:
   - This directory includes some generic plots of all data; this is
     mainly meant for quick checking

   `DataFiles`:
   - There, the adjusted csv files for the actual comparison with the
     `PMC-LBL` data are located.


### 7. Compare with `PMC-LBL`

   After these steps, one needs to follow a similar process to prepare
   the `PMC-LBL` data within the folder `03_Simulation_LBL_PMC`.

   The process is very similar compared to the one described here; the
   main difference is that one does not calculated anything anymore,
   but rather focuses on the post-processing of the snapshots.
   
   This approach allows flexible later adjustments of additional
   post-processing within the version controlled repository.  Further
   details for the process is described in the relevant folder.
## Step by Step description to compare an `OpenFOAM` simulation


### 1. Got to folder
   `/02_Simulation_Base/OpenFOAM_mapped_Snapshots`
   
   This is the link to the [folder](/FM_Burner/02_Simulation_Base/OpenFOAM_mapped_Snapshots).

   There you find scripts and some folders.  
   
   The `constant` folder and the `system` folder are needed for the
   OpenFOAM to run the case. E.g. in the `system/controlDict` on need
   to define the time range and can also refer to the post-processing
   of some monitor points. Both of these files will be copied to the
   actual case directories during the whole process.


### 2. Download Snapshots from Github releases

   The actual data for each snapshot is available within different
   github releases. The can be dowloaded manually or by exeecuting the
   script:

   `bash 00_download_files.sh`
   
   This script creates a directory called `Release` and will download
   the snapshots into this folder.
   

### 3. Creating Case directories for each time step   
  
   At the moment, the approach is setup to run each time snapshot in
   separate directory. To arrange these directories and to copy the
   already mentioned `system` and `constant` folder to the case, one
   has tor execture:
   
   `python 01_createCaseFolder_separate.py`
   
   The other option is to use:
   `python 02_createCaseFolder_combined.py`
  
   This combines all snapshots into one combined case directory; but
   this is not used further here.
  

### 4. Distribute an adjusted `controlDict`

   Once a case snapshot structure is created, the `controlDict` will
   be copied to these directories with an adjustment of the end time
   for the simulation.
   
   `python 03_adjust_copy_OPF_controlDict.py`


### 5. Run all cases

   The next step is to run all snapshots with
 
   `python 04_run_OPF.py`
 
   Obviously, the settings within the `system` and `constant` files
   can should be adjusted as it is needed before the simulation.

   By default, the script assumes, that your
   `OpenFOAM`-`fireRadFoam_MaCFP` installation is accessable (in your
   `PATH`) with the name `fireRadFoam_MaCFP`; if this is not the case
   try to run the simulation via:
 
   `python 04_run_OPF.py <complete_path_to_OpenFOAM_user_bin/fireRadFoam_MaCFP`


### 6. Post-Processing of all Snapshots 

   To run the post-processing for all snapshots, go into the `POST` directory
   
   `cd POST`
   
   and
   
   execute the python script
   
   `python 00_post_Extract_Data_and_Plot_Line_OPF.py`

   This script will do the actual post-processing of the
   calculations. It is prepared in a way to have similar name
   structure like for the other setups for `FDS` and for `PMC-LBL`.

   Two directories, one with the name `LinePlots` and the other one
   with the name `DataFiles` are created.
   
   `LinePlots`:
   - This directory includes some generic plots of all data; this is mainly meant for quick checking

   `DataFiles`:
   - There, the adjusted csv files for the actual comparison with the `PMC-LBL` data are located.


### 7. Compare with `PMC-LBL`
   After these steps, one needs to follow a similar process to prepare
   the `PMC-LBL` data within the folder `03_Simulation_LBL_PMC`.

   The process is very similar compared to the one described here; the
   main difference is that one does not calculated anything anymore,
   but rather focuses on the post-processing of the snapshots.
   
   This approach allows flexible later adjustments of additional
   post-processing within the version controlled repository.

   Further details for the process is described in the relevant
   folder.


## Step by Step description to post-process the `PMC-LBL` results


### 1. Got to folder
   `cd 03_Simulation_LBL_PMC`
   
   This is the link to the [folder](/FM_Burner/03_Simulation_LBL_PMC).

   There you find scripts and some folders.  
   
   The `constant` folder and the `system` folder are needed for the
   OpenFOAM to run the post-processing for each case. E.g. in the
   `system/controlDict` one needs to define the the post-processing of
   some monitor points. These directories will be copied to the actual
   case directories during the whole process.


### 2. Download Snapshots-Results from Github releases

   The actual data for each snapshot is available within different
   github releases. The can be dowloaded manually or by exeecuting the
   script:

   `bash 00_download_files.sh`
   
   This script creates a directory called `Release` and will download
   the snapshots into this folder.
   

### 3. Creating Case directories for each time step   
  
   At the moment, the approach is setup to run each time snapshot in
   separate directory. To arrange these directories and to copy the
   already mentioned `system` and `constant` folder to the case, one
   has tor execture:
   
   `python 01_createCaseFolder_separate.py`
   

### 4. Distribute a run script for the post-processing

   Once a case snapshot structure is created, the `run_POST.sh` will
   be copied to these directories.
   
   `python 02_copy_run_POST.py`


### 5. Post-Process all cases

   The next step is to post-process all snapshots with
   
   `python 03_run_OPF_postProcess.py`
   

   Here, the settings within the `system` and `constant` files should
   not be adjusted as the data is only post-process; any adjustment
   would not have any impact on the results.



### 6. Post-Processing of all Snapshots 

   To run the post-processing for all snapshots, go into the `POST` directory
   
   `cd POST`
   
   and
   
   execute the python script
   
   `python 00_post_Extract_Data_and_Plot_Line_PMC.py`

   This script will do the actual post-processing of the
   calculations. It is prepared in a way to have similar name
   structure like for the other setups for `FDS` and for `OpenFOAM`.

   Two directories, one with the name `LinePlots` and the other one
   with the name `DataFiles` are created.
   
   `LinePlots`:
   - This directory includes some generic plots of all data; this is mainly meant for quick checking

   `DataFiles`:
   - There, the adjusted csv files for the actual comparison with the `PMC-LBL` data are located.



## Step by Step description compare `FDS` and `OpenFOAM` reuslts with `PMC-LBL` benchmark
