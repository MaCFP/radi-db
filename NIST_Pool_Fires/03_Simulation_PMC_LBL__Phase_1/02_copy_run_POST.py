import shutil
# ==============================================================================
templateF = "controlDict.Template"
pattern = "endTime_Val"

timeL = ["5.00009","10.0001","15.0004","20.0003","25.0001","30.0002","35.0002","40.0001","45.0004","50.0005","55.0001","60.0005","65.0001","70.0004","75.0002","80.0003","85","90.0005","95.0002","100","105","110","115.001","120","125","130","135","140","145","150","155","160","165","170","175","180","185","190","195","200"]
timeL = ["5.00009","10.0001","15.0004"]



# ==============================================================================
for i, time in enumerate(timeL):
        # dirF= "./Release/Cases/Case_Time_"+str(time)
        dirF= "./Release/Case_Time_"+str(time)
        shutil.copy("run_POST.sh", dirF)
        # with open(templateF,'r') as f:
        #     newlines = f.read()
        #     endTimeValue = float(time)+ 0.0000002
        #     newlines = newlines.replace(pattern, str(endTimeValue))
        # # with open(dirF + "/system/controlDict", 'w') as f_out:
        # #     f_out.write(newlines)
        # # f_out.close()
        # f.close()
