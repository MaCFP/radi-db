
# General Information

General overview about the folder structure is described in the main `README.md` file.

## Experimental data

The main directory for the FM-Burner is in the `macfp-db` project:
https://github.com/MaCFP/macfp-db/tree/master/Extinction/FM_Burner

There, the experimental setup for the `FM-Burner` is described in detail: 
https://github.com/MaCFP/macfp-db/tree/master/Extinction/FM_Burner/Documentation


And e.g. available experimental data is located at:
https://github.com/MaCFP/macfp-db/tree/master/Extinction/FM_Burner/Experimental_Data


# Description for validating FDS and OpenFOAM with the PMC-LBL solution
It is assumed that a basic understanding about the FDS and OpenFOAM setup is already available for further descriptions.

## Step by Step description to compare an OpenFOAM simulation

1. Got to folder
   `/02_Simulation_Base/OpenFOAM_mapped_Snapshots`
   
   There you find scripts and some folders. 
   The `constant` folder and the `system` folder are needed for the OpenFOAM to run the case. E.g. in the `system/controlDict` on need to define the time range and can also refer to the post-processing of some monitor points. Both of these files will be copied to the actual case directories during the whole process.

2. Download Snapshots from Github releases

   The actual data for each snapshot is available within different github releases. The can be dowloaded manually or by exeecuting the script:

   `bash 00_download_files.sh`
   
   This script creates a directory called `Release` and will download the snapshots into this folder.
   
3. Creating Case directories for each time step   
  
   At the moment, the approach is setup to run each time snapshot in separate directory. To arrange these directories and to copy the already mentioned `system` and `constant` folder to the case, one has tor execture:
   
   `python 01_createCaseFolder_separate.py`
   
  The other option is to use:
  `python 02_createCaseFolder_combined.py`
  
  This combines all snapshots into one combined case directory; but this is not used further here.
  
4. Distribute an adjusted `controlDict`

   Once a case snapshot structure is created, the `controlDict` will be copied to these directories with an adjustment of the end time for the simulation.
   
   `python 03_adjust_copy_OPF_controlDict.py`

5. Run all cases


 The next step is to run all snapshots with
 
 `python 04_run_OPF.py`
 
  Obviously, the settings within the `system` and `constant` files can should be adjusted as it is needed before the simulation.

6. Post-Processing of all Snapshots 

   To run the post-processing for all snapshots, go into the `POST` directory
   
   `cd POST`
   
   and
   
   execute the python script
   
   `python 00_post_Extract_Data_and_Plot_Line_OPF.py`

   This script will do the actual post-processing of the calculations. It is prepared in a way to have similar name structure like for the other setups for `FDS` and for `PMC-LBL`.

   Two directories, one with the name `LinePlots` and the other one with the name `DataFiles` are created.
   
   `LinePlots`:
   - This directory includes some generic plots of all data; this is mainly meant for quick checking

   `DataFiles`:
   - There, the adjusted csv files for the actual comparison with the `PMC-LBL` data are located.

7. Compare with `PMC-LBL`
   After these steps, one needs to follow a similar process to prepare the `PMC-LBL` data within the folder `03_Simulation_LBL_PMC`.
   The process is very similar compared to the one described here; the main difference is that one does not calculated anything anymore, but rather focuses on the post-processing of the snapshots.
   
   This approach allows flexible later adjustments of additional post-processing within the version controlled repository.
   Further details for the process is described in the relevant folder.
