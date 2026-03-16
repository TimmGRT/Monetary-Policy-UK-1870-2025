# INDICATIONS PAR RAPPORT AUX DONNES 
# Au sein de ce fichier les données seront stockés et compressés en parquet (une méthode plus légere et plus rapide que des CSV).
# Je m'occuperai de les compressés quand on les aura, c'est très facile vous verrez

# Maintenant pour telecharger des données du datalake dans vos zone de code attribués, vous executerez le code suivant 

import pandas as pd
path_parquet_file = 'le chemin exact du parquet que vous voulez, vous devez faire un clique droit sur le parquet désiré et > "Copy Path" '
df = pd.read_parquet(path_parquet_file)

