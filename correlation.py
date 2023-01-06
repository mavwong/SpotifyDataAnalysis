##########################################
#   ___ __  __ ___  ___  ___ _____ ___   #
#  |_ _|  \/  | _ \/ _ \| _ |_   _/ __|  #
#   | || |\/| |  _| (_) |   / | | \__ \  #
#  |___|_|  |_|_|  \___/|_|_\ |_| |___/  #
#                                        #
##########################################

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from pandas import DataFrame, Series

#############################################
#   ___ _____ _   _  _ ___   _   ___ ___    #
#  / __|_   _/_\ | \| |   \ /_\ | _ |   \   #
#  \__ \ | |/ _ \| .` | |) / _ \|   | |) |  #
#  |___/ |_/_/ \_|_|\_|___/_/ \_|_|_|___/   #
#                                           #
#############################################

PATH_ROOT =     Path(__file__).parent
PATH_OUTPUT =   PATH_ROOT / "output"
PATH_DATA =     PATH_ROOT / "data"
PATH_NTBK =     PATH_ROOT / "notebook"

#########################################################
#   ___  ___ ___ ___ _  _ ___ _____ ___ ___  _  _ ___   #
#  |   \| __| __|_ _| \| |_ _|_   _|_ _/ _ \| \| / __|  #
#  | |) | _|| _| | || .` || |  | |  | | (_) | .` \__ \  #
#  |___/|___|_| |___|_|\_|___| |_| |___\___/|_|\_|___/  #
#                                                       #
#########################################################


def create_correlation(input_df:DataFrame, name:str):
    all_correlation = ["spearman", "kendall", "pearson"]
    
    for corr in all_correlation:
        plt.figure(figsize=(16,10), dpi=720)
        df_corr = input_df.corr(method=corr)
        
        fig = sns.heatmap(df_corr, annot=True, cmap="inferno", center=0)
        fig.set(title=f"{name.title()} - {corr.title()} Correlation Heatmap")
        plt.savefig(PATH_OUTPUT / f"{name}_data-{corr}_corr.png")
        
        
def data_correlation(file_input: Path, file_name:str=None):
    if not isinstance(file_input, Path):
        file_input = Path(file_input)
    
    # Read CSV
    df = pd.read_csv(file_input)
    
    # Create correlation
    create_correlation(df, name=file_input.stem if file_name == None else file_name)
    


######################################
#   ___ ___  ___   ___ ___ ___ ___   #
#  | _ | _ \/ _ \ / __| __/ __/ __|  # 
#  |  _|   | (_) | (__| _|\__ \__ \  #
#  |_| |_|_\\___/ \___|___|___|___/  #
#                                    #
######################################

if __name__ == "__main__":
    None