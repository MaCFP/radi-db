# ..............................................................................
import pandas as pd
import numpy as np

# ..............................................................................
import matplotlib.pyplot as plt

# ..............................................................................
import glob
import os

# src = '/home/ihritik/file.txt'
# dst = '/home/ihritik/Desktop/file(symlink).txt'
# os.symlink(src, dst)
  
# print("Symbolic link created successfully")

timeL = ["5.00009","10.0001","15.0004","20.0003","25.0001","30.0002","35.0002","40.0001","45.0004","50.0005","55.0001","60.0005","65.0001","70.0004","75.0002","80.0003","85","90.0005","95.0002","100","105","110","115.001","120","125","130","135","140","145","150","155","160","165","170","175","180","185","190","195","200"]
timeL = ["5.00009","10.0001","15.0004","20.0003"]
timeL = ["5.00009","10.0001"]

calcL = ["FDS_1","OPF_1","PMC_LBL"]
calcAvgNameL = ["FDS_1_Avg","OPF_1_Avg","PMC_LBL_Avg"]

tool_prefixL = ["FDS","OPF","PMC_LBL"]

time_prefix = "Case_Time_"

# dataDir = "/Volumes/PortableSSD/00_MaCFP/RAD_Subgroup/01_radi-db.git/FM_Burner/02_Simulation_Base/FDS_mapped_Snapshots/POST/LinePlots/"
dataDir = "./DataFiles/"


dfz = pd.read_csv("Mapping_Fields.csv")
# ...................................................................................
print (100*".")
print (dfz.head())
print (20*".")
print (dfz.tail())

# ==============================================================================
for q, toolprefix in enumerate(tool_prefixL):
    for n, time in enumerate(timeL):
        for i, name in enumerate(dfz['name'].values):
            print (100*"=")
            print (100*"=")
            print("name: ",name)
        
            # ==============================================================================
            # PMC
            fieldName = dfz[tool_prefixL[q]][i]
            globPattern = tool_prefixL[q] +"_" + time_prefix + "*" + name + "*" + fieldName
            print("globPattern: ",globPattern)
            globPattern = os.path.join(dataDir,calcL[q],globPattern)+"*"
            print("globPattern: ",globPattern)
            calcAvgL = glob.glob(globPattern)
            print("Directories for Avg: ",calcAvgL)
    
            # ...................................................................................
            dfL = []
            for p, csv in enumerate(calcAvgL):
                df = pd.read_csv(csv,index_col=0)
                print (100*".")
                print (df.head())
                print (20*".")
                print (df.tail())
                print (100*".")
                print (df.columns)
                colL = []
                timeStr = csv.split("_Time_")[1].split("__")[0]
                print("timeStr: ",timeStr)
                for col in df.columns:
                    colL.append(col+"_"+timeStr)
                df.columns = colL
                print (100*".")
                print (df.head())
                print (20*".")
                print (df.tail())
                print (100*".")
                print (df.columns)
                dfL.append(df)
            dfall = pd.concat(dfL,axis=1)
            dfall[fieldName+"_MEAN"] = dfall.mean(axis=1)
            # ...................................................................................
            print (100*".")
            print (dfall.head())
            print (20*".")
            print (dfall.tail())
            dfMean = dfall.filter(regex=".*MEAN")
            # ...................................................................................
            print (100*".")
            print (dfMean.head())
            print (20*".")
            print (dfMean.tail())
    
            name2 = os.path.join(dataDir,calcAvgNameL[q],name + "_MEAN__"+fieldName+".csv")
            print(name2)
            dfMean.to_csv(name2)


    
#         # ==============================================================================
#         # FDS 
#         caclAvgL = glob.glob(tool_prefixL[0] +"_" + time_prefix + time +"*")
#         print("Directories for Avg: ",calcAvgL)
#         fieldName = dfz[tool_prefixL[0]][i]
#         # name2 = tool_prefixL[0] +"_" + time_prefix + timeL[0] + "__"+name + "__"+fieldName+".csv"
#         name2 = tool_prefixL[0] +"_" + time_prefix + time + "__"+name + "__"+fieldName+".csv"
#         print("name: ",name2)
#         total_name = os.path.join(calcL[0] , name2)
#         print("total_name: ",total_name)
    
#         # ...................................................................................
#         df = pd.read_csv(os.path.join("DataFiles",total_name))
#         print (100*".")
#         print (df.columns)
    
#         # ==============================================================================
#         # OPF
#         caclAvgL = glob.glob(tool_prefixL[1] +"_" + time_prefix + time +"*")
#         print("Directories for Avg: ",calcAvgL)
#         fieldName = dfz[tool_prefixL[1]][i]
#         # name2 = tool_prefixL[1] +"_" + time_prefix + timeL[0] + "__"+name + "__"+fieldName+".csv"
#         name2 = tool_prefixL[1] +"_" + time_prefix + time + "__"+name + "__"+fieldName+".csv"
#         print("name: ",name2)
#         total_name = os.path.join(calcL[1] , name2)
#         print("total_name: ",total_name)
    
#         # ...................................................................................
#         df = pd.read_csv(os.path.join("DataFiles",total_name))
#         print (100*".")
#         print (df.columns)
#         # headerRow = "1"
#         # dataRow = "2"
#         # # x_ColN = df.index.name
#         # x_ColN = df.columns[0]
#         # y_ColN = df.columns[1]
#         # dataLabel = "OPF" 
#         # markerStyle = "-."
#         # print (total_name)
#         # print (headerRow)
#         # print (dataRow)
#         # print (x_ColN)
#         # print (y_ColN)
        
#         # opf_part = total_name+","+headerRow+","+dataRow+","+x_ColN+","+y_ColN+","+dataLabel+","+markerStyle
    
#         # # ..............................................................................
#         # print(dfz)
#         # dfz = dfz.fillna("-")
#         # print(dfz)
#         # print(dfz.columns)
#         # y_min = dfz["ymin"][i]
#         # y_max= dfz["ymax"][i]
#         # x_Label = dfz["xAxes"][i]
#         # y_Label = dfz["yAxes"][i]
#         # title = dfz["title"][i]
#         # # title = "Title"
#         # # x_Label = "x-Position (m)"
#         # # y_Label = "Field (unit)"
#         # # x_min = 0
#         # # x_max = 10
#         # # y_min= 10
#         # # y_max = 10
#         # legendPosition = "upper right"
#         # # pdfName = timeL[0] + "_" + name +"__"+fieldName + ".pdf"
#         # pdfName = time + "_" + name +"__"+fieldName + ".pdf"
#         # plotStyle_part = title +","+x_Label + "," + y_Label +"," + str(x_min) + "," + str(x_max) + ","+str(y_min)+"," + str(y_max)+","+legendPosition+","+pdfName
#         # file1.write(pmc_part+"\n")
# #         file1.write(pmc_part + ","+ fds_part+ ","+plotStyle_part+"\n")
# #         file1.write(pmc_part + ","+ opf_part+ ","+plotStyle_part+"\n")
# # file1.close()

