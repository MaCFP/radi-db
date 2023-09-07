# ............................................................................t.
import pandas as pd
import numpy as np

# ..............................................................................
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

# ..............................................................................
import glob
import os

# ..............................................................................
# plt.rc('axes', axisbelow=True)

debug = False

# ==============================================================================
def createDir(dirName):
    if not(os.path.isdir(dirName)):
        try:
            os.makedirs(dirName)
        except OSError as e:
            if e.errno != 17:
                raise
            pass

# ==============================================================================
postDir = "./LinePlots"
createDir(postDir)

postDir0 = "./DataFiles/"
createDir(postDir0)

# ==============================================================================
# rootDir = "/Volumes/PortableSSD/00_MaCFP/RAD_Subgroup/01_radi-db.git/FM_Burner/02_Simulation_Base/FDS_mapped_Snapshots/xxx_Release_xxx/"
rootDir = "/Volumes/PortableSSD/00_MaCFP/RAD_Subgroup/01_radi-db.git/FM_Burner/02_Simulation_Base/FDS_mapped_Snapshots/Release/"

caseL = glob.glob(rootDir+"/Case_Time_*")
print(caseL)

csvN = "FM_15cm_Burner_C2H4_20p9_5mm_line.csv"
print("csvN: ",csvN)

# ==============================================================================
for n, case in enumerate(caseL):
    dat = case +"/"+ csvN
    print("dat: ",dat)

    rootCase = os.path.basename(case)
    postDir1 = postDir + "/"+rootCase +"/"
    createDir(postDir1)

    df = pd.read_csv(dat, skiprows=1)
    print(df.head())
    step = 1

    # for colStep in range(0,int(72/2)):
    for colStep in range(0,int(168/2)):
        print (100*"=")
        print(colStep)
        print(step)
        dfposunits = pd.read_csv(dat, skiprows=0,usecols=[step*colStep,step*colStep+1],index_col=0,nrows=1)
        print(dfposunits.head())
        print(dfposunits.columns)
        print(dfposunits.index)
        # exit()
        df = pd.read_csv(dat, skiprows=1,usecols=[step*colStep,step*colStep+1],index_col=0)
        print(df.head())
        print(df.columns)
        colN = df.columns[0]
        print(colN)
        if "RHF" in colN:
            print("exti")
            print (colN)
            df = df * 1000.0
            # exit()
        step = 2
        postDir2 = postDir1 + df.columns[0] +"/"
        createDir(postDir2)
        print(postDir2)
        colN1 = colN.split("__")[1]
        colN0 = df.columns[0]
        df.columns = [colN1]
        df.to_csv(postDir2+colN0+".csv")
        print(case)
        df.to_csv(postDir0+"FDS_"+rootCase+"__"+colN0+".csv")

        df.plot()
        plt.ylabel(colN1+ " ("+ dfposunits.columns[0].split(".")[0] +")")
        plt.xlabel(dfposunits.index[0]+"-Position (m)")
        plt.grid(linestyle = "dashed")
        plt.savefig(postDir2+colN0+".png")
