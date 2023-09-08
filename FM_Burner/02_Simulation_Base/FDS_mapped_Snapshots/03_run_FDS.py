import os
import subprocess
import sys
# ==============================================================================
templateF = "v0_FM_15cm_Burner_C2H4_20p9_5mm.fds"

timeL = ["5.00009","10.0001","15.0004","20.0003","25.0001","30.0002","35.0002","40.0001","45.0004","50.0005","55.0001","60.0005","65.0001","70.0004","75.0002","80.0003","85","90.0005","95.0002","100","105","110","115.001","120","125","130","135","140","145","150","155","160","165","170","175","180","185","190","195","200"]

try:
   command = sys.argv[1]
except:
   print ("Default command...")
   command = "fds"
print("Command: ", command)

# ==============================================================================
timeStepL =  range(1,41)

initDir = os.getcwd()

for i, timeStep in enumerate(timeStepL):
        # dirF= "./Release/Case_Time_"+str(timeL[i])+"_Step"+str(timeStep)
        print(100*"-")
        dirF= "./Release/Case_Time_"+str(timeL[i])
        print(dirF)
        os.chdir(dirF)
        # print(os.getcwd())
        # simRunFile = dirF+"/"+templateF
        simRunFile = templateF
        # print(simRunFile)
        p=subprocess.Popen([command,simRunFile], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,)
        command_output = p.communicate()[0]
        log_file = open('fds_run.log', 'a')
        log_file.write('\n')
        log_file.write(str(command_output))
        os.chdir(initDir)
