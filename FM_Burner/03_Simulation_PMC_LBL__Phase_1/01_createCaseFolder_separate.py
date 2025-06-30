import glob
import os
import tarfile
import shutil

# ==============================================================================
def createDir(newDir):
    if not(os.path.isdir(newDir)):
        try:
            os.makedirs(newDir)
        except OSError as e:
            if e.errno != 17:
                raise
            pass

# ==============================================================================
os.chdir("./Release/")
tarL = glob.glob("*.tar.gz")
# print(tarL)

# ------------------------------------------------------------------------------
for i, tar in enumerate(tarL):
    print(100*"=")
    print(tar)
    timeStep=tar.split(".tar.gz")[0]
    ftar = tarfile.open(tar)
    ftar.extractall('./')
    ftar.close()
    if timeStep != "constant_polyMesh" and timeStep != "SpectralRad":
        dirName = "Case_Time_"+str(timeStep)
        print("Creating directory: ", dirName)
        createDir(dirName)
        shutil.move(timeStep,dirName)
        # os.rename(timeStep,dirName)

# ==============================================================================
caseL = glob.glob("Case_Time_*")
# print(caseL)
print("")
print (100*"=")
print("")
print ("Copying - constant, polyMesh and system directories...")
for case in caseL:
    # print(case)
    # os.symlink("../../constant",case + "/constant")
    # os.symlink("./constant/polyMesh",case + "/constant/polyMesh")
    shutil.copytree("../constant",case + "/constant", dirs_exist_ok=True)
    shutil.copytree("./constant/polyMesh",case + "/constant/polyMesh", dirs_exist_ok=True)
    shutil.copytree("../system",case + "/system", dirs_exist_ok=True)



