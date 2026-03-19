# INDICATIONS PAR RAPPORT AUX DONNES 
# Au sein de ce fichier les données seront stockés et compressés en parquet (une méthode plus légere et plus rapide que des CSV).
# Je m'occuperai de les compressés quand on les aura, c'est très facile vous verrez
# Maintenant pour telecharger des données du datalake dans vos zone de code attribués, vous executerez le code suivant :

# import pandas as pd
# path_parquet_file = 'le chemin exact du parquet que vous voulez, vous devez faire un clique droit sur le parquet désiré et > "Copy Path" '
# df = pd.read_parquet(path_parquet_file)



########### CODE ###########

### Scripts telechargement des datas 
from global_macro_data import gmd
from IPython.display import display
import os
from pathlib import Path
import pandas as pd
from fredapi import Fred


## FONCTIONS POUR TELECHARGEMENT d'un DF avec global macro data
def data_download_gmd(country : str):
    try :
        df = gmd(version="2025_01", country=country)
        return df

    except Exception as e:
        print("WARNING, CHECK BACK THE PARAMETERS : {e}")

def data_download_fred(indicator : str, start : str , end : str):

    fred = Fred(api_key="7001389dfc7179ce6bbfe18fd28ad5ac")

    data = fred.get_series(series_id=indicator, observation_start=start, observation_end= end)

    df = pd.DataFrame(data)

    return(df)


## FONCTTION POUR STORER UN DF DANS LE DATALAKE EN PARQUET
def data_storing(data, nom_fichier : str):
    # recherche du path du datalake
    CURRENT_FILE_PATH = Path(__file__).resolve()
    DATALAKE_PATH = CURRENT_FILE_PATH.parent

    # telechargement du df en parquet vers datalake_path
    file_name = nom_fichier + '.parquet'

    PARQUET_FILE_PATH = DATALAKE_PATH/"PARQUET_FOLDER"/file_name

    try :
        if not isinstance(data, pd.DataFrame):
            df = pd.DataFrame(data)
        else:
            df = data

        if nom_fichier in which_parquet():
            a = input(f"are you sure you want to erase and replace the file {nom_fichier} : 'yes' or 'no'")
            if a == 'yes':
                PARQUET_FILE_PATH.unlink()
                data_storing(data, nom_fichier)
            
        df.to_parquet(PARQUET_FILE_PATH, engine='pyarrow', compression='snappy')

    except Exception as e:
        print(f"Warning to the file that you entered... Should be a dataframe : {e}")
    return

## FONCTION POUR DOWNLOAD DES DONNÉES PARQUERT DANS VOTRE ZONE DE CODE 

def import_parquet(file_name : str):
    CURRENT_FILE_PATH = Path(__file__).resolve()
    DATALAKE_PATH = CURRENT_FILE_PATH.parent
    PARQUET_FOLDER_PATH = DATALAKE_PATH/"PARQUET_FOLDER"

    try: 
        for f in PARQUET_FOLDER_PATH.iterdir():
            if str(f.stem) == file_name:
                df = pd.read_parquet(f)

    except Exception as e:
        print(f"something didn't work, please retry after checking the name of the file searched : {e}")

    return df


## FONCION POUR SAVOIR QUELS SONT LES PARQUETS DISPO DANS LA BD 

def which_parquet():
    CURRENT_FILE_PATH = Path(__file__).resolve()
    DATALAKE_PATH = CURRENT_FILE_PATH.parent
    PARQUET_FOLDER_PATH = DATALAKE_PATH/"PARQUET_FOLDER"

    list_file = [f.stem for f in PARQUET_FOLDER_PATH.iterdir()]
    print(f"les fichiers disponibles dans la BD sont : {list_file}")


# ## GUIDE des fonctions du module local datalake

# from DATALAKE.data import *

# data = data_download_gmd("country") -> Telechargement des données liés à un pays via global_macro_dataset (BD publique)
# data = data_download_fred("indicator" : str, "start" : str , "end" : str) -> Telechargement d'un indicateur via la FRED (BD publique)

# data_storing(data : dataframe, "nom_fichier" : str) -> Range un dataframe "data" dans le DATALAKE en parquet, que vous venez de télécharger d'internet 

# data = import_parquet("file_name" : str) -> importe un dataframe du DATALAKE dans votre file cible (notebook ou .py)

# which_parquet() -> Vous renvoie une liste de l'ensemble des parquets dispo dans le DATALAKE








    

    
    
    
