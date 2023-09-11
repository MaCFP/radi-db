import os


import glob
import os, errno

def force_symlink(file1, file2):
    try:
        print("standard..")
        os.symlink(file1, file2)
    except OSError as e:
        print("remove..")
        if e.errno == errno.EEXIST:
            os.remove(file2)
            os.symlink(file1, file2)


fdsDir = "../../../02_Simulation_Base/FDS_mapped_Snapshots/POST/DataFiles/"
csvL = glob.glob(fdsDir+"*.csv")
for n, csv in enumerate(csvL):
    # os.symlink(csv,"./DataFiles/FDS_1/"+os.path.basename(csv))
    force_symlink("../../"+csv,"./DataFiles/FDS_1/"+os.path.basename(csv))

opfDir = "../../../02_Simulation_Base/OpenFOAM_mapped_Snapshots/POST/DataFiles/"
csvL = glob.glob(opfDir+"*.csv")
for n, csv in enumerate(csvL):
    # os.symlink(csv,"./DataFiles/OPF_1/"+os.path.basename(csv))
    force_symlink("../../"+csv,"./DataFiles/OPF_1/"+os.path.basename(csv))

pmcDir = "../../../03_Simulation_LBL_PMC/POST/DataFiles/"
csvL = glob.glob(pmcDir+"*.csv")
for n, csv in enumerate(csvL):
    # print(csv)
    # os.symlink(csv,"./DataFiles/PMC_LBL/"+os.path.basename(csv))
    force_symlink("../../"+csv,"./DataFiles/PMC_LBL/"+os.path.basename(csv))
