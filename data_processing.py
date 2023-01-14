##########################################
#   ___ __  __ ___  ___  ___ _____ ___   #
#  |_ _|  \/  | _ \/ _ \| _ |_   _/ __|  #
#   | || |\/| |  _| (_) |   / | | \__ \  #
#  |___|_|  |_|_|  \___/|_|_\ |_| |___/  #
#                                        #
##########################################

from pandas import DataFrame, Series
from datetime import date

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

from relative_path import PATH_OUTPUT_GRAPH, PATH_OUTPUT_PROF
from pandas_profiling import ProfileReport

#############################################
#   ___ _____ _   _  _ ___   _   ___ ___    #
#  / __|_   _/_\ | \| |   \ /_\ | _ |   \   #
#  \__ \ | |/ _ \| .` | |) / _ \|   | |) |  #
#  |___/ |_/_/ \_|_|\_|___/_/ \_|_|_|___/   #
#                                           #
#############################################

TODAY = date.today()
DATE_FORMAT = str(TODAY.year) + str(TODAY.month) + str(TODAY.day)

# Turn interactive plotting off
plt.ioff()

#########################################################
#   ___  ___ ___ ___ _  _ ___ _____ ___ ___  _  _ ___   #
#  |   \| __| __|_ _| \| |_ _|_   _|_ _/ _ \| \| / __|  #
#  | |) | _|| _| | || .` || |  | |  | | (_) | .` \__ \  #
#  |___/|___|_| |___|_|\_|___| |_| |___\___/|_|\_|___/  #
#                                                       #
#########################################################


# Redundant to pandas-profiling
def export_correlation(input_df:DataFrame, name:str, export:bool = False):
    all_correlation = ["spearman", "kendall", "pearson"]
    
    for corr in all_correlation:
        plt.figure(figsize=(16,10), dpi=720)
        df_corr = input_df.corr(method=corr)
        
        fig = sns.heatmap(df_corr, annot=True, cmap="inferno", center=0)
        fig.set(title=f"{name.title()} - {corr.title()} Correlation Heatmap")
        
        if export:
            corr_name = f"{DATE_FORMAT}-{name}Data_Corr{corr.title()}.png"
            plt.savefig(PATH_OUTPUT_GRAPH / corr_name)
            plt.close("all")

def export_profiling(input_df:DataFrame, name:str) -> ProfileReport:
    profile = ProfileReport(input_df, title=name)
    
    profile_name = f"{DATE_FORMAT}-{name}Data_Profiling.html"
    profile.to_file(PATH_OUTPUT_PROF / profile_name)

class VisualizeMissing:
    def __init__(
            self, 
            input_df:DataFrame, 
            name:str, export:bool=False, 
            process_null:bool=False, 
            process_zero:bool=False
        ) -> None:
        
        self.df:DataFrame = input_df.copy(deep=True)
        self._process_data(replace_null=process_null, replace_zero=process_zero)
        self.name = name.title()
        
        self._export = export
        self._fontsize = 16
        
        self._label_rotation:int = 90
        self._figsize:int = (30,15)
        self._about:str = "Visualize Missing, NA, 0 values"
        
    def _process_data(self, replace_null:bool, replace_zero:bool):
        """ Process the dataframe. """
        if replace_null:
            self.df.replace("", np.NaN, inplace=True)
        if replace_zero:
            self.df.replace(0,  np.NaN, inplace=True)
    
    def Bar(self):
        fig = msno.bar(
            df = self.df, 
            fontsize = self._fontsize,
            label_rotation = self._label_rotation,
            figsize = self._figsize
        )
        
        chart_name = f"{self.name} Data - Bar Chart - {self._about}"
        fig_name = f"{DATE_FORMAT}-{self.name}Data_BarChart-NullExplore.png"
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
        
        chart_name = f"{self.name} Data - Matrix Chart - {self._about}"
        fig_name = f"{DATE_FORMAT}-{self.name}Data_MatrixChart-NullExplore.png"
        fig.set(title=chart_name)
        
        if self._export:
            plt.savefig(PATH_OUTPUT_GRAPH / fig_name)
        return plt.show()
    
    def Heatmap(self):
        fig = msno.heatmap(
            df = self.df, 
            fontsize = self._fontsize,
            label_rotation = self._label_rotation,
            figsize = self._figsize
        )
        
        chart_name = f"{self.name} Data - Heatmap Chart - {self._about}"
        fig_name = f"{DATE_FORMAT}-{self.name}Data_HeatmapChart-NullExplore.png"
        fig.set(title=chart_name)
        
        if self._export:
            plt.savefig(PATH_OUTPUT_GRAPH / fig_name)
        return plt.show()

######################################
#   ___ ___  ___   ___ ___ ___ ___   #
#  | _ | _ \/ _ \ / __| __/ __/ __|  # 
#  |  _|   | (_) | (__| _|\__ \__ \  #
#  |_| |_|_\\___/ \___|___|___|___/  #
#                                    #
######################################

if __name__ == "__main__":
    None