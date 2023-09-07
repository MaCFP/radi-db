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
calcL = ["FDS_1","OPF_1","PMC_LBL","FDS_1_AVG","OPF_1_AVG","PMC_LBL_AVG"]

tool_prefixL = ["FDS","OPF","PMC_LBL","FDS","OPF","PMC_LBL"]

time_prefix = "Case_Time_"

# dataDir = "/Volumes/PortableSSD/00_MaCFP/RAD_Subgroup/01_radi-db.git/FM_Burner/02_Simulation_Base/FDS_mapped_Snapshots/POST/LinePlots/"
dataDir = "./DataFiles/"


dfz = pd.read_csv("Mapping_Fields.csv")
# ...................................................................................
print (100*".")
print (dfz.head())
print (20*".")
print (dfz.tail())

file1 = open("PlotConfig.csv", "w")
file1.write("Exp_Filename,Exp_Header_Row,Exp_Data_Row,Exp_x_Col_Name,Exp_y_Col_Name,Exp_Data_Label,Exp_Marker_Style,Cmp_Filename,Cmp_Header_Row,Cmp_Data_Row,Cmp_x_Col_Name,Cmp_y_Col_Name,Cmp_Data_Label,Cmp_Line_Style,Plot_Title,Plot_x_Label,Plot_y_Label,Plot_x_Min,Plot_x_Max,Plot_y_Min,Plot_y_Max,Plot_Legend_Location,Plot_Filename\n")

for n, time in enumerate(timeL):
    for i, name in enumerate(dfz['name'].values):
        print (100*"=")
        print (100*"=")
        print("name: ",name)
    
        # ==============================================================================
        # PMC
        fieldName = dfz[tool_prefixL[2]][i]
        # name2 = tool_prefixL[2] +"_" + time_prefix + timeL[0] + "__"+name + "__"+fieldName+".csv"
        name2 = tool_prefixL[2] +"_" + time_prefix + time + "__"+name + "__"+fieldName+".csv"
        print("name: ",name2)
        total_name = os.path.join(calcL[2] , name2)
        print("total_name: ",total_name)
    
        # ...................................................................................
        df = pd.read_csv(os.path.join("DataFiles",total_name))
        print (100*".")
        print (df.head())
        print (20*".")
        print (df.tail())
        print (100*".")
        print (df.columns)
        headerRow = "1"
        dataRow = "2"
        x_ColN = df.columns[0]
        y_ColN = df.columns[1]
        dataLabel = "PMC" 
        markerStyle = "o"
        print (total_name)
        print (headerRow)
        print (dataRow)
        print (x_ColN)
        print (y_ColN)
    
        x_min = df[df.columns[0]].min()
        x_max = df[df.columns[0]].max()
        # y_min = df[df.columns[1]].min()
        # y_max = df[df.columns[1]].max()
    
    
        pmc_part = total_name+","+headerRow+","+dataRow+","+x_ColN+","+y_ColN+","+dataLabel+","+markerStyle
    
        # ==============================================================================
        # FDS 
        fieldName = dfz[tool_prefixL[0]][i]
        # name2 = tool_prefixL[0] +"_" + time_prefix + timeL[0] + "__"+name + "__"+fieldName+".csv"
        name2 = tool_prefixL[0] +"_" + time_prefix + time + "__"+name + "__"+fieldName+".csv"
        print("name: ",name2)
        total_name = os.path.join(calcL[0] , name2)
        print("total_name: ",total_name)
    
        # ...................................................................................
        df = pd.read_csv(os.path.join("DataFiles",total_name))
        print (100*".")
        print (df.columns)
        headerRow = "1"
        dataRow = "2"
        # x_ColN = df.index.name
        x_ColN = df.columns[0]
        y_ColN = df.columns[1]
        dataLabel = "FDS" 
        markerStyle = "-"
        print (total_name)
        print (headerRow)
        print (dataRow)
        print (x_ColN)
        print (y_ColN)
    
        fds_part = total_name+","+headerRow+","+dataRow+","+x_ColN+","+y_ColN+","+dataLabel+","+markerStyle
    
        # ==============================================================================
        # OPF
        fieldName = dfz[tool_prefixL[1]][i]
        # name2 = tool_prefixL[1] +"_" + time_prefix + timeL[0] + "__"+name + "__"+fieldName+".csv"
        name2 = tool_prefixL[1] +"_" + time_prefix + time + "__"+name + "__"+fieldName+".csv"
        print("name: ",name2)
        total_name = os.path.join(calcL[1] , name2)
        print("total_name: ",total_name)
    
        # ...................................................................................
        df = pd.read_csv(os.path.join("DataFiles",total_name))
        print (100*".")
        print (df.columns)
        headerRow = "1"
        dataRow = "2"
        # x_ColN = df.index.name
        x_ColN = df.columns[0]
        y_ColN = df.columns[1]
        dataLabel = "OPF" 
        markerStyle = "-."
        print (total_name)
        print (headerRow)
        print (dataRow)
        print (x_ColN)
        print (y_ColN)
        
        opf_part = total_name+","+headerRow+","+dataRow+","+x_ColN+","+y_ColN+","+dataLabel+","+markerStyle
    
        # ..............................................................................
        print(dfz)
        dfz = dfz.fillna("-")
        print(dfz)
        print(dfz.columns)
        y_min = dfz["ymin"][i]
        y_max= dfz["ymax"][i]
        x_Label = dfz["xAxes"][i]
        y_Label = dfz["yAxes"][i]
        title = dfz["title"][i]
        # title = "Title"
        # x_Label = "x-Position (m)"
        # y_Label = "Field (unit)"
        # x_min = 0
        # x_max = 10
        # y_min= 10
        # y_max = 10
        legendPosition = "upper right"
        # pdfName = timeL[0] + "_" + name +"__"+fieldName + ".pdf"
        pdfName = time + "_" + name +"__"+fieldName + ".pdf"
        plotStyle_part = title +","+x_Label + "," + y_Label +"," + str(x_min) + "," + str(x_max) + ","+str(y_min)+"," + str(y_max)+","+legendPosition+","+pdfName
        # file1.write(pmc_part+"\n")
        file1.write(pmc_part + ","+ fds_part+ ","+plotStyle_part+"\n")
        file1.write(pmc_part + ","+ opf_part+ ","+plotStyle_part+"\n")
        
# for n, time in enumerate(timeL):
for i, name in enumerate(dfz['name'].values):
    print (100*"=")
    print (100*"=")
    print("name: ",name)
    # ==============================================================================
    # ==============================================================================
    # PMC AVG
    fieldName = dfz[tool_prefixL[2]][i]
    print(name)
    name2 = name + "_MEAN__"+fieldName+".csv"
    print("name: ",name2)
    total_name = os.path.join(calcL[5] , name2)
    print("total_name: ",total_name)

    # ...................................................................................
    df = pd.read_csv(os.path.join("DataFiles",total_name))
    print (100*".")
    print (df.head())
    print (20*".")
    print (df.tail())
    print (100*".")
    print (df.columns)
    headerRow = "1"
    dataRow = "2"
    x_ColN = df.columns[0]
    y_ColN = df.columns[1]
    dataLabel = "PMC" 
    markerStyle = "o"
    print (total_name)
    print (headerRow)
    print (dataRow)
    print (x_ColN)
    print (y_ColN)

    x_min = df[df.columns[0]].min()
    x_max = df[df.columns[0]].max()
    # y_min = df[df.columns[1]].min()
    # y_max = df[df.columns[1]].max()


    pmc_part = total_name+","+headerRow+","+dataRow+","+x_ColN+","+y_ColN+","+dataLabel+","+markerStyle

    # ==============================================================================
    # FDS 
    # fieldName = dfz[tool_prefixL[0]][i]
    # # name2 = tool_prefixL[0] +"_" + time_prefix + timeL[0] + "__"+name + "__"+fieldName+".csv"
    # name2 = tool_prefixL[0] +"_" + time_prefix + time + "__"+name + "__"+fieldName+".csv"
    # print("name: ",name2)
    # total_name = os.path.join(calcL[3] , name2)
    # print("total_name: ",total_name)

    fieldName = dfz[tool_prefixL[0]][i]
    print(name)
    name2 = name + "_MEAN__"+fieldName+".csv"
    print("name: ",name2)
    total_name = os.path.join(calcL[3] , name2)
    print("total_name: ",total_name)

    # ...................................................................................
    df = pd.read_csv(os.path.join("DataFiles",total_name))
    print (100*".")
    print (df.columns)
    headerRow = "1"
    dataRow = "2"
    # x_ColN = df.index.name
    x_ColN = df.columns[0]
    y_ColN = df.columns[1]
    dataLabel = "FDS" 
    markerStyle = "-"
    print (total_name)
    print (headerRow)
    print (dataRow)
    print (x_ColN)
    print (y_ColN)

    fds_part = total_name+","+headerRow+","+dataRow+","+x_ColN+","+y_ColN+","+dataLabel+","+markerStyle

    # ==============================================================================
    # OPF
    fieldName = dfz[tool_prefixL[1]][i]
    print(name)
    name2 = name + "_MEAN__"+fieldName+".csv"
    print("name: ",name2)
    total_name = os.path.join(calcL[4] , name2)
    print("total_name: ",total_name)
    # fieldName = dfz[tool_prefixL[1]][i]
    # # name2 = tool_prefixL[1] +"_" + time_prefix + timeL[0] + "__"+name + "__"+fieldName+".csv"
    # name2 = tool_prefixL[1] +"_" + time_prefix + time + "__"+name + "__"+fieldName+".csv"
    # print("name: ",name2)
    # total_name = os.path.join(calcL[4] , name2)
    # print("total_name: ",total_name)

    # ...................................................................................
    df = pd.read_csv(os.path.join("DataFiles",total_name))
    print (100*".")
    print (df.columns)
    headerRow = "1"
    dataRow = "2"
    # x_ColN = df.index.name
    x_ColN = df.columns[0]
    y_ColN = df.columns[1]
    dataLabel = "OPF" 
    markerStyle = "-."
    print (total_name)
    print (headerRow)
    print (dataRow)
    print (x_ColN)
    print (y_ColN)
    
    opf_part = total_name+","+headerRow+","+dataRow+","+x_ColN+","+y_ColN+","+dataLabel+","+markerStyle

    # ..............................................................................
    print(dfz)
    dfz = dfz.fillna("-")
    print(dfz)
    print(dfz.columns)
    y_min = dfz["ymin"][i]
    y_max= dfz["ymax"][i]
    x_Label = dfz["xAxes"][i]
    y_Label = dfz["yAxes"][i]
    title = dfz["title"][i]
    # title = "Title"
    # x_Label = "x-Position (m)"
    # y_Label = "Field (unit)"
    # x_min = 0
    # x_max = 10
    # y_min= 10
    # y_max = 10
    legendPosition = "upper right"
    # pdfName = timeL[0] + "_" + name +"__"+fieldName + ".pdf"
    pdfName = "MEAN_" + name +"__"+fieldName + ".pdf"
    plotStyle_part = title +","+x_Label + "," + y_Label +"," + str(x_min) + "," + str(x_max) + ","+str(y_min)+"," + str(y_max)+","+legendPosition+","+pdfName
    # file1.write(pmc_part+"\n")
    file1.write(pmc_part + ","+ fds_part+ ","+plotStyle_part+"\n")
    file1.write(pmc_part + ","+ opf_part+ ","+plotStyle_part+"\n")
file1.close()
    
