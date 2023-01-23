##########################################
#   ___ __  __ ___  ___  ___ _____ ___   #
#  |_ _|  \/  | _ \/ _ \| _ |_   _/ __|  #
#   | || |\/| |  _| (_) |   / | | \__ \  #
#  |___|_|  |_|_|  \___/|_|_\ |_| |___/  #
#                                        #
##########################################

from pathlib import Path
import pandas as pd
from pandas import DataFrame, Series

from relative_path import PATH_DATA, PATH_OUTPUT_DATA, PATH_OUTPUT_GRAPH, PATH_OUTPUT_PROF

#############################################
#   ___ _____ _   _  _ ___   _   ___ ___    #
#  / __|_   _/_\ | \| |   \ /_\ | _ |   \   #
#  \__ \ | |/ _ \| .` | |) / _ \|   | |) |  #
#  |___/ |_/_/ \_|_|\_|___/_/ \_|_|_|___/   #
#                                           #
#############################################

#########################################################
#   ___  ___ ___ ___ _  _ ___ _____ ___ ___  _  _ ___   #
#  |   \| __| __|_ _| \| |_ _|_   _|_ _/ _ \| \| / __|  #
#  | |) | _|| _| | || .` || |  | |  | | (_) | .` \__ \  #
#  |___/|___|_| |___|_|\_|___| |_| |___\___/|_|\_|___/  #
#                                                       #
#########################################################


def convert_csv_parquet(input_path:Path) -> None:
    """ Convert CSV file to Parquet. """
    if not isinstance(input_path, Path):
        input_path = Path(input_path)
    
    df = pd.read_csv(input_path)
    output = input_path.parent / f"{input_path.stem}.parquet"
    df.to_parquet(output, engine="pyarrow")


def export_top_values(input_df:DataFrame, col_to_sort:str, col_needed:list=None, sample_size:int=10) -> DataFrame:
    """ Export the top data. 
    - input_df: input dataframe
    - col_to_sort: sorting the dataframe by this column
    - col_needed: drop any col not define.
    """
    df_sorted = input_df.sort_values(col_to_sort, ascending=False)
    df_sorted.reset_index(drop=True, inplace=True)
    if col_needed != None:
        df_sorted = df_sorted[col_needed]
    
    df_result = df_sorted.head(sample_size)
    df_result.to_csv(PATH_OUTPUT_DATA / f"top_{sample_size}_{col_to_sort}.csv")
    return df_result


######################################
#   ___ ___  ___   ___ ___ ___ ___   #
#  | _ | _ \/ _ \ / __| __/ __/ __|  # 
#  |  _|   | (_) | (__| _|\__ \__ \  #
#  |_| |_|_\\___/ \___|___|___|___/  #
#                                    #
######################################

if __name__ == "__main__":
    None