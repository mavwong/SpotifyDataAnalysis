##########################################
#   ___ __  __ ___  ___  ___ _____ ___   #
#  |_ _|  \/  | _ \/ _ \| _ |_   _/ __|  #
#   | || |\/| |  _| (_) |   / | | \__ \  #
#  |___|_|  |_|_|  \___/|_|_\ |_| |___/  #
#                                        #
##########################################

from pathlib import Path
from pandas import DataFrame, Series

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

from relative_path import PATH_OUTPUT_GRAPH

#############################################
#   ___ _____ _   _  _ ___   _   ___ ___    #
#  / __|_   _/_\ | \| |   \ /_\ | _ |   \   #
#  \__ \ | |/ _ \| .` | |) / _ \|   | |) |  #
#  |___/ |_/_/ \_|_|\_|___/_/ \_|_|_|___/   #
#                                           #
#############################################

def create_correlation(input_df:DataFrame, name:str, export:bool = False):
    all_correlation = ["spearman", "kendall", "pearson"]
    
    for corr in all_correlation:
        plt.figure(figsize=(16,10), dpi=720)
        df_corr = input_df.corr(method=corr)
        
        fig = sns.heatmap(df_corr, annot=True, cmap="inferno", center=0)
        fig.set(title=f"{name.title()} - {corr.title()} Correlation Heatmap")
        
        if export:
            plt.savefig(PATH_OUTPUT_GRAPH / f"{name}_data-{corr}_corr.png")
            

class VisualizeMissing:
    def __init__(self, input_df:DataFrame, name:str, export:bool=False) -> None:
        self.df:DataFrame = input_df.copy(deep=True)
        self.name = name.title()
        
        self._export = export
        self._fontsize = 16
        
        self._label_rotation:int = 90
        self._figsize:int = (30,15)
        
        self._about:str = "Visualize Missing, NA, 0 values"
        
    def __post_init__(self):
        """ Post process the dataframe. """
        self.df.replace("", np.NaN, inplace=True)
        self.df.replace(0,  np.NaN, inplace=True)
    
    def Bar(self):
        fig = msno.bar(
            df = self.df, 
            fontsize = self._fontsize,
            label_rotation = self._label_rotation,
            figsize = self._figsize
        )
        
        chart_name = f"{self.name} - Bar Chart - {self._about}"
        fig_name = f"{self.name}Data_Matrix_Missing.png"
        fig.set(title=chart_name)
        
        if self._export:
            plt.savefig(PATH_OUTPUT_GRAPH / fig_name)
        return plt.show()
    
    def Matrix(self):
        fig = msno.matrix(
            df = self.df, 
            fontsize = self._fontsize,
            label_rotation = self._label_rotation,
            figsize = self._figsize
        )
        
        chart_name = f"{self.name}-Matrix Chart-{self._about}"
        fig_name = f"{self.name}Data_Matrix_Missing.png"
        fig.set(title=chart_name)
        
        if self._export:
            plt.savefig(PATH_OUTPUT_GRAPH + fig_name)
        return plt.show()
    
    def Heatmap(self):
        fig = msno.heatmap(
            df = self.df, 
            fontsize = self._fontsize,
            label_rotation = self._label_rotation,
            figsize = self._figsize
        )
        
        chart_name = f"{self.name} - Heatmap Chart - {self._about}"
        fig_name = f"{self.name}Data_Heatmap_Missing.png"
        fig.set(title=chart_name)
        
        if self._export:
            plt.savefig(PATH_OUTPUT_GRAPH + fig_name)
        return plt.show()


#########################################################
#   ___  ___ ___ ___ _  _ ___ _____ ___ ___  _  _ ___   #
#  |   \| __| __|_ _| \| |_ _|_   _|_ _/ _ \| \| / __|  #
#  | |) | _|| _| | || .` || |  | |  | | (_) | .` \__ \  #
#  |___/|___|_| |___|_|\_|___| |_| |___\___/|_|\_|___/  #
#                                                       #
#########################################################

######################################
#   ___ ___  ___   ___ ___ ___ ___   #
#  | _ | _ \/ _ \ / __| __/ __/ __|  # 
#  |  _|   | (_) | (__| _|\__ \__ \  #
#  |_| |_|_\\___/ \___|___|___|___/  #
#                                    #
######################################

if __name__ == "__main__":
    None