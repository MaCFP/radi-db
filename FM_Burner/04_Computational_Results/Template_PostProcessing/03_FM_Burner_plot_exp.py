#!/usr/bin/env python3
# McDermott
# Feb 2021

# first, make sure the macfp module directory is in your path
# if not, uncomment the lines below and replace <path to macfp-db>
# with the path (absolute or relative) to your macfp-db repository

import sys
# sys.path.append('<path to macfp-db>/macfp-db/Utilities/')
# sys.path.append('../../../../macfp-db/Utilities/')
# sys.path.append('/Users/fbraenns/09_TOOLs_Application/MaCFP/00_Repositories/macfp-db_fork/Utilities/')

import macfp
import importlib
importlib.reload(macfp) # use for development (while making changes to macfp.py)
import matplotlib.pyplot as plt

# macfp.dataplot(config_filename='FM_Burner_Dataplot_Config.csv',
macfp.dataplot(config_filename='PlotConfig.csv',
               institute=' ',
               revision=' ',
               expdir='./DataFiles/',
               cmpdir='./DataFiles/',
               pltdir='./Plots/',
               close_figs=True,
               verbose=True,
               plot_list=['all'])

