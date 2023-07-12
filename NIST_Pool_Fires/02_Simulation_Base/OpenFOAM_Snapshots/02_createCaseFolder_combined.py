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
tarL = glob.glob("*.tar.gz")

# ------------------------------------------------------------------------------
dirName = "Case_Time_ALL"
createDir(dirName)
for i, tar in enumerate(tarL):
    print(100*"=")
    print(tar)
    timeStep=tar.split(".tar.gz")[0]
    ftar = tarfile.open(tar)
    ftar.extractall('./')
    ftar.close()
    if timeStep != "constant_polyMesh":
        shutil.move(timeStep,dirName)
        # shutil.rmtree(timeStep)

# ==============================================================================
shutil.copytree("constant",dirName+ "/constant", dirs_exist_ok=True)
shutil.copytree("system",dirName+ "/system", dirs_exist_ok=True)
shutil.copytree("constant_polyMesh/polyMesh",dirName+ "/constant/polyMesh", dirs_exist_ok=True)



