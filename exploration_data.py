##########################################
#   ___ __  __ ___  ___  ___ _____ ___   #
#  |_ _|  \/  | _ \/ _ \| _ |_   _/ __|  #
#   | || |\/| |  _| (_) |   / | | \__ \  #
#  |___|_|  |_|_|  \___/|_|_\ |_| |___/  #
#                                        #
##########################################


from pandas import DataFrame
import pandas as pd
from datetime import date

import numpy as np
import matplotlib.pyplot as plt
import missingno as msno
from typing import Any

from pandas_profiling import ProfileReport
from relative_path import OUTPUT_MISSING, OUTPUT_EXPLORE

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


class AutoExploratoryAnalysis:
    def __init__(self, input_df:DataFrame, name:str) -> None:
        self.df:DataFrame = input_df
        self.name = name.title()
        
    def create_profiling(self) -> ProfileReport:
        profile = ProfileReport(self.df, title=f"{self.name} Data")
        
        profile_name = f"{DATE_FORMAT}-{self.name}Data_Profiling.html"
        profile.to_file(OUTPUT_EXPLORE / profile_name)
        

class CountMissingData:
    """ Get the missing data count and percentage based on input dataframe. """
    
    def __init__(self, input_df:DataFrame) -> DataFrame:
        self.df = input_df
        
    def get(self):
        total = self.df.isnull().sum().sort_values(ascending=False)
        percent = (self.df.isnull().sum()/self.df.isnull().count()).sort_values(ascending=False)
        missing_data = pd.concat([total, percent], axis=1, keys=['TotalMissing', 'Percent%'])
        return missing_data
        

class VisualizeMissing:
    def __init__(
            self, 
            input_df:DataFrame, 
            name:str, 
            
            export_plot:bool=False, 
            show_plot:bool=False,
            
            process_null:bool=False, 
            process_zero:bool=False
        ) -> None:
        
        self.df:DataFrame = input_df
        self._process_data(replace_null=process_null, replace_zero=process_zero)
        self.name = name.title()
        
        self._export = export_plot
        self._show = show_plot
        
        self._fontsize:int = 16
        self._label_rotation:int = 90
        self._figsize:int = (30,15)
        
        self._about:str = "Visualize Missing, NA, 0 values"
        plt.ioff()
        
        
    def _process_data(self, replace_null:bool, replace_zero:bool):
        """ Process the dataframe. """
        if replace_null:
            self.df.replace("", np.NaN, inplace=True)
        if replace_zero:
            self.df.replace(0,  np.NaN, inplace=True)
            
    def _saving_and_showing(self, _name:str, _show:bool) -> Any:
        if self._export:
            plt.savefig(OUTPUT_MISSING / _name)
        
        # Show or Hide Plot
        if self._show or _show:
            plt.show()
        else:
            plt.close("all")
        
    def Bar(self, show:bool=False):
        fig = msno.bar(
            df = self.df, 
            fontsize = self._fontsize,
            label_rotation = self._label_rotation,
            figsize = self._figsize
        )
        
        chart_name = f"{self.name} Data - Bar Chart - {self._about}"
        fig_name = f"{DATE_FORMAT}-{self.name}Data_BarChart-NullExplore.png"
        fig.set(title=chart_name)
        
        # Save or Show the results
        self._saving_and_showing(_name = fig_name, _show = show)
    
    
    def Matrix(self, show:bool=False):
        fig = msno.matrix(
            df = self.df, 
            fontsize = self._fontsize,
            label_rotation = self._label_rotation,
            figsize = self._figsize
        )
        
        chart_name = f"{self.name} Data - Matrix Chart - {self._about}"
        fig_name = f"{DATE_FORMAT}-{self.name}Data_MatrixChart-NullExplore.png"
        fig.set(title=chart_name)
        
        # Save or Show the results
        self._saving_and_showing(_name = fig_name, _show = show)
    
    def Heatmap(self, show:bool=False):
        fig = msno.heatmap(
            df = self.df, 
            fontsize = self._fontsize,
            label_rotation = self._label_rotation,
            figsize = self._figsize
        )
        
        chart_name = f"{self.name} Data - Heatmap Chart - {self._about}"
        fig_name = f"{DATE_FORMAT}-{self.name}Data_HeatmapChart-NullExplore.png"
        fig.set(title=chart_name)
        
        # Save or Show the results
        self._saving_and_showing(_name = fig_name, _show = show)
    

######################################
#   ___ ___  ___   ___ ___ ___ ___   #
#  | _ | _ \/ _ \ / __| __/ __/ __|  # 
#  |  _|   | (_) | (__| _|\__ \__ \  #
#  |_| |_|_\\___/ \___|___|___|___/  #
#                                    #
######################################

if __name__ == "__main__":
    None