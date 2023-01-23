##########################################
#   ___ __  __ ___  ___  ___ _____ ___   #
#  |_ _|  \/  | _ \/ _ \| _ |_   _/ __|  #
#   | || |\/| |  _| (_) |   / | | \__ \  #
#  |___|_|  |_|_|  \___/|_|_\ |_| |___/  #
#                                        #
##########################################

from typing import List, Dict

import pandas as pd
from pandas import DataFrame

#########################################################
#   ___  ___ ___ ___ _  _ ___ _____ ___ ___  _  _ ___   #
#  |   \| __| __|_ _| \| |_ _|_   _|_ _/ _ \| \| / __|  #
#  | |) | _|| _| | || .` || |  | |  | | (_) | .` \__ \  #
#  |___/|___|_| |___|_|\_|___| |_| |___\___/|_|\_|___/  #
#                                                       #
#########################################################


def preprocess_df(input_df:DataFrame, sort_by:str, copy:bool=False) -> DataFrame:
    """ Preprocess dataframe: sorting data, reseting index, etc. """
    if copy:
        result_df = input_df.copy()
    else:
        result_df = input_df
    
    result_df.sort_values(by=sort_by, ascending=False, inplace=True)
    result_df.reset_index(drop=True, inplace=True)
    return result_df

def isolate_columns(input_df:DataFrame, feature_cols:List[str], merge_in:str="id") -> DataFrame:
    """ Isolate or separate main and feature dataframe. """
    df = input_df.copy()
    cols_df = list(df.columns)
    
    # Get the main_cols
    main_cols = []
    for col in cols_df:
        if not col in feature_cols:
            main_cols.append(col)
            
    # main dataframe vs feature dataframe
    df_main = df[main_cols]
    
    feature = [merge_in] + feature_cols
    df_feature = df[feature]
    return df_main, df_feature

def remove_characters(string:str, special_char:str = None):
    if special_char == None:
        special_char = "@#$*&"
        
    lst_special_char = [x for x in special_char]
    result = "".join(filter(lambda char: char not in lst_special_char , string))
    return result


######################################
#   ___ ___  ___   ___ ___ ___ ___   #
#  | _ | _ \/ _ \ / __| __/ __/ __|  # 
#  |  _|   | (_) | (__| _|\__ \__ \  #
#  |_| |_|_\\___/ \___|___|___|___/  #
#                                    #
######################################

if __name__ == "__main__":
    None