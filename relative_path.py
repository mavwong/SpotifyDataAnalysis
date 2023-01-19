##########################################
#   ___ __  __ ___  ___  ___ _____ ___   #
#  |_ _|  \/  | _ \/ _ \| _ |_   _/ __|  #
#   | || |\/| |  _| (_) |   / | | \__ \  #
#  |___|_|  |_|_|  \___/|_|_\ |_| |___/  #
#                                        #
##########################################

from pathlib import Path

#############################################
#   ___ _____ _   _  _ ___   _   ___ ___    #
#  / __|_   _/_\ | \| |   \ /_\ | _ |   \   #
#  \__ \ | |/ _ \| .` | |) / _ \|   | |) |  #
#  |___/ |_/_/ \_|_|\_|___/_/ \_|_|_|___/   #
#                                           #
#############################################

PATH_ROOT =     Path(__file__).parent
PATH_DATA =     PATH_ROOT / "data"
PATH_RAW_DATA = PATH_DATA / "raw_data"
PATH_PROC_DATA = PATH_DATA / "processed_data"

PATH_OUTPUT =   PATH_ROOT / "output"
PATH_OUTPUT_DATA = PATH_OUTPUT / "data"
PATH_OUTPUT_GRAPH = PATH_OUTPUT / "graph"
PATH_OUTPUT_PROF = PATH_OUTPUT / "profiling"

TRACK_DATA =    PATH_RAW_DATA / "tracks.parquet"
ARTIST_DATA =   PATH_RAW_DATA / "artists.parquet"

PROCESSED_TRACK_DATA =  PATH_PROC_DATA / "tracks_processed.parquet"
PROCESSED_ARTIST_DATA = PATH_PROC_DATA / "artists_processed.parquet"
PROCESSED_FEATURE_DATA = PATH_PROC_DATA / "features_processed.parquet"

FEATURE_COLS = ['danceability', 'energy', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature']

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