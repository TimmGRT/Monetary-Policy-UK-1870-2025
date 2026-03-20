import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt


### créé un histogramme pour le dataframe "df" et la colonne que vous souhaitez, attention, fonctionne seulement si vous utilisez le df qui vient de "main_cleaned.parquet" car la fonction récupère "year"
def histogram(df, column: str):
    try:
        df[column].hist(bins=20, edgecolor='black')
        plt.ticklabel_format(style='plain', axis='x')
        plt.xlabel("Valeur")
        plt.ylabel("Nombre d'occurences")
        plt.show()
    except Exception as e: 
        print(f"Erreur : {e}")

### créé un graphique d'évolution dans le temps de la variable column qui se trouve dans le dataframe "df"
def time_evo (df,column: str):
    try:
        plt.plot(df['year'], df[column])
        plt.ticklabel_format(style='plain', axis='y')
        plt.xlabel("Temps")
        plt.ylabel("Valeur")
        plt.show()
    except Exception as e: 
        print(f"Erreur : {e}")
    
if __name__ == "__main__":
    print("Vous êtes bien dans le fichier outils_eda")