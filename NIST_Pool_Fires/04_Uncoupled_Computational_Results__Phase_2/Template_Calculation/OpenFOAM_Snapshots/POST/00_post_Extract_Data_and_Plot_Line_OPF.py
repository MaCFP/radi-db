# ..............................................................................
import pandas as pd
import numpy as np

# ..............................................................................
import matplotlib.pyplot as plt

# ..............................................................................
import glob
import os

# ..............................................................................
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
rootDir = "/Volumes/PortableSSD/00_MaCFP/RAD_Subgroup/01_radi-db.git/FM_Burner/02_Simulation_Base/OpenFOAM_mapped_Snapshots/Release/"

caseL = glob.glob(rootDir+"/Case_Time_*")
# caseL = glob.glob(rootDir+"/v_Case_Time_*")

# ==============================================================================
postDir = "./LinePlots"
createDir(postDir)

# ==============================================================================
csvFluidInitL = ["initFields_DO_h_x_n06_06_y_0_z_1524_1D___cell.sets",
"initFields_DO_h_x_n06_06_y_0_z_2286_15D___cell.sets",
"initFields_DO_h_x_n06_06_y_0_z_3048_2D___cell.sets",
"initFields_DO_h_x_n06_06_y_0_z_3810_25D___cell.sets",
"initFields_DO_h_x_n06_06_y_0_z_4572_3D___cell.sets",
"initFields_DO_h_x_n06_06_y_0_z_5334_35D___cell.sets",
"initFields_DO_v_x0_y_0_z_0_83___cell.sets"]

csvWallL = ["radFields_IN_FIRE_h_x_0_y_n006_006_z_0__cellPoint.sets",
"radFields_IN_FIRE_h_x_n006_006_y0_z_0__cellPoint.sets",
"radFields_IN_h_z1__x_n06_06_y0_z_n37__cellPoint.sets",
"radFields_OUT_h_z2__x_n06_06_y0_z_83__cellPoint.sets",
"radFields_WW_h_x2__x06_y_n06_06_z_3__cellPoint.sets",
"radFields_WW_v_x2__x06_y0_z_0_83__cellPoint.sets"]

csvFluidL = ["radFields_DO_h_x_n06_06_y_0_z_1524_1D__cell.sets",
"radFields_DO_h_x_n06_06_y_0_z_2286_15D__cell.sets",
"radFields_DO_h_x_n06_06_y_0_z_3048_2D__cell.sets",
"radFields_DO_h_x_n06_06_y_0_z_3810_25D__cell.sets",
"radFields_DO_h_x_n06_06_y_0_z_4572_3D__cell.sets",
"radFields_DO_h_x_n06_06_y_0_z_5334_35D__cell.sets",
"radFields_DO_v_x0_y_0_z_0_83__cell.sets"]


csvAllL = [csvFluidL,csvWallL,csvFluidInitL]

# ------------------------------------------------------------------------------
posFluidL = ["x-","x-","x-","x-","x-","x-","z-"]
posWallL = ["y-","x-","x-","x-","y-","z-"]
posInitFluidL = ["x-","x-","x-","x-","x-","x-","z-"]

posAllL = [posFluidL,posWallL,posInitFluidL]

# ------------------------------------------------------------------------------
fieldFluidRADL = ["G","a"]
fieldWallRADL = ["qin","qr","qem"]
fieldInitL = ["C2H4","CO","CO2","H2O","N2","O2","soot","T","rho"]

fieldAllL = [fieldFluidRADL, fieldWallRADL, fieldInitL]

# ------------------------------------------------------------------------------
# unitsFluidRADL = ["kg/s^3","1/m"]
# kg/s^3 = W/m^2
unitsFluidRADL = ["kg/s^3","1/m"]
unitsWallRADL = ["kg/s^3","kg/s^3","kg/s^3"]
unitsInitL = ["-","-","-","-","-","-","K","kg/m3","-"]
# Qdot kg/ms^3

unitsAllL = [unitsFluidRADL, unitsWallRADL, unitsInitL]

# ==============================================================================
for i, case in enumerate(caseL):
    postDir0 = "./DataFiles/"
    createDir(postDir0)
    postDir1 = "./LinePlots/"+ os.path.basename(case)
    createDir(postDir1)
    print (100*"=")
    print("Case: ",case)
    # ..............................................................................
    for n, csvL in enumerate(csvAllL):
        if debug:
            print (100*"-")
        # ..............................................................................
        for m, csv in enumerate(csvL):
            timeL = glob.glob(case+"/postProcessing/"+csv+"/*")
            csvLN = glob.glob(timeL[0]+"/*.csv")
            df = pd.read_csv(csvLN[0],index_col=0)
            if debug:
                print (100*".")
                print(csvLN[0])
                print(df.head())

            postDir3 = os.path.join(postDir1 , os.path.basename(csv)+"_ALL")
            createDir(postDir3)

            df.plot()
            plt.savefig(postDir3 +"/"+ csv+"_ALL.png")
            plt.close()

            # ..............................................................................
            postDir2 = os.path.join(postDir1 , os.path.basename(csv))
            createDir(postDir2)
            for p,colN in enumerate(df.columns):
                # df[colN].to_csv(postDir2 +"/"+ csv+"_"+colN+".csv")
                rootCase = os.path.basename(case)
                # print(csv)
                # print(csv.split("__cell.sets"))
                if len(csv.split("___cell.sets")) > 1:
                    csvNew = csv.split("___cell.sets")[0]
                elif len(csv.split("__cell.sets")) > 1:
                    csvNew = csv.split("__cell.sets")[0]
                else:
                    csvNew = csv.split("__cellPoint.sets")[0]
                # exit()
                df[colN].to_csv(postDir0 +"/OPF_"+rootCase +"__"+ csvNew +"__"+colN+".csv")

                df[colN].plot()
                plt.ylabel(colN + " ("+ unitsAllL[n][p] +")")
                plt.xlabel(posAllL[n][m]+"Position (m)")
                plt.grid(linestyle = "dashed")
                plt.savefig(postDir2 +"/"+ csv+"_"+colN+".png")
                plt.close()
