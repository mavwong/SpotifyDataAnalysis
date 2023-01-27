##########################################
#   ___ __  __ ___  ___  ___ _____ ___   #
#  |_ _|  \/  | _ \/ _ \| _ |_   _/ __|  #
#   | || |\/| |  _| (_) |   / | | \__ \  #
#  |___|_|  |_|_|  \___/|_|_\ |_| |___/  #
#                                        #
##########################################

from pandas import DataFrame
from datetime import date
import matplotlib.pyplot as plt

from typing import Any, List
from relative_path import OUTPUT_FEATURE

import plotly.graph_objects as go
import plotly.offline as pyo

from pathlib import Path

#############################################
#   ___ _____ _   _  _ ___   _   ___ ___    #
#  / __|_   _/_\ | \| |   \ /_\ | _ |   \   #
#  \__ \ | |/ _ \| .` | |) / _ \|   | |) |  #
#  |___/ |_/_/ \_|_|\_|___/_/ \_|_|_|___/   #
#                                           #
#############################################

TODAY = date.today()
DATE_FORMAT = str(TODAY.year) + str(TODAY.month) + str(TODAY.day)

#########################################################
#   ___  ___ ___ ___ _  _ ___ _____ ___ ___  _  _ ___   #
#  |   \| __| __|_ _| \| |_ _|_   _|_ _/ _ \| \| / __|  #
#  | |) | _|| _| | || .` || |  | |  | | (_) | .` \__ \  #
#  |___/|___|_| |___|_|\_|___| |_| |___\___/|_|\_|___/  #
#                                                       #
#########################################################
    
    
class VisualizeFeatureColumns:
    def __init__(
            self, 
            input_df:DataFrame, 
            name:str, 
            feature_cols:List[str], 
            criteria:int, 
            export_plot:bool=False, 
            show_plot:bool=False,
            output_path = OUTPUT_FEATURE
        ) -> None:
        
        self.df = input_df
        self.name = name
        
        self._feature = feature_cols
        self._criteria = criteria
        
        self._export = export_plot
        self._show = show_plot
        
        self.output_path = self._process_path(output_path)
        
        self._process_df()
        plt.ioff()
        
    def _process_path(self, input_path) -> Path:
        """ Preprocess path. """
        if isinstance(input_path, str):
            return Path(input_path)
        
    def _process_df(self) -> DataFrame:
        self.df.sort_values(by=self._criteria, ascending=False, inplace=True)
        self.df.reset_index(drop=True, inplace=True)
        
    def _compute_rows_percent(self, percentage=100):
        rows, _ = self.df.shape
        return int(rows*(percentage/100))
    
    def _saving_and_showing(self, figure, _name:str, _show:bool) -> Any:
        if self._export:
            figure.savefig(self.output_path / _name)
        
        # Show or Hide Plot
        if self._show or _show:
            figure.show()
        else:
            figure.close("all")
    
    def TopDataByPercent(self, show:bool=False):
        top_10 = self._compute_rows_percent(10)
        top_25 = self._compute_rows_percent(25)
        
        fig = go.Figure(
        data=[
            go.Scatterpolar(r=self.df[self._feature].head(top_10).median(), theta=self._feature, fill='toself', opacity=0.6, name="Top 10%"),
            go.Scatterpolar(r=self.df[self._feature].head(top_25).median(), theta=self._feature, fill='toself', opacity=0.6, name="Top 25%"),
        ],
        layout=go.Layout(
            title=go.layout.Title(text=f"Median: Feature comparison based on {self._criteria.title()} data percentage."),
            polar={'radialaxis': {'visible':True}},
            showlegend=True
            )
        )
        
        fig_name = f"{DATE_FORMAT}-{self.name}Data_PolarFeatureByCount.png"
        self._saving_and_showing(figure=fig, _name = fig_name, _show = show)
        
    def TopDataByCount(self, show:bool=False):
        fig = go.Figure(
        data=[
            go.Scatterpolar(r=self.df[self._feature].head(100).median(), theta=self._feature, fill='toself', opacity=0.6, name="Top 100"),
            go.Scatterpolar(r=self.df[self._feature].head(10).median(), theta=self._feature, fill='toself', opacity=0.6, name="Top 10"),
            go.Scatterpolar(r=self.df[self._feature].median(), theta=self._feature, fill='toself', opacity=0.6, name='All'),
        ],
        layout=go.Layout(
            title=go.layout.Title(text=f"Median: Feature comparison based on {self._criteria.title()} data count."),
            polar={'radialaxis': {'visible':True}},
            showlegend=True
            )
        )
        fig_name = f"{DATE_FORMAT}-{self.name}Data_PolarFeatureByPerct.png"
        self._saving_and_showing(figure=fig, _name = fig_name, _show = show)


######################################
#   ___ ___  ___   ___ ___ ___ ___   #
#  | _ | _ \/ _ \ / __| __/ __/ __|  # 
#  |  _|   | (_) | (__| _|\__ \__ \  #
#  |_| |_|_\\___/ \___|___|___|___/  #
#                                    #
######################################

if __name__ == "__main__":
    None