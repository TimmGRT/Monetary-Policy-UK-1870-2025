import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns


### créé un histogramme pour le dataframe "df" et la colonne que vous souhaitez, attention, fonctionne seulement si vous utilisez le df qui vient de "main_cleaned.parquet" car la fonction récupère "year"
def histogram(df, column: str):
    try:
        df[column].hist(bins=20, edgecolor='black')
        plt.ticklabel_format(style='plain', axis='x')
        plt.xlabel("Valeur")
        plt.ylabel("Nombre d'occurences")
        plt.show()
        plt.close()
    except Exception as e: 
        print(f"Erreur dans l'histogramme: {e}")

### créé un graphique d'évolution dans le temps de la variable column qui se trouve dans le dataframe "df"
def time_evo (df,column: str):
    try:
        plt.plot(df['year'], df[column])
        plt.ticklabel_format(style='plain', axis='y')
        plt.xlabel("Temps")
        plt.ylabel("Valeur")
        plt.show()
        plt.close()
    except Exception as e: 
        print(f"Erreur dans le graphique d'évolution: {e}")

### créé un scatter plot pour les variables x et y du dataframe "df"
def scat (df,x: str,y: str):
    try:
        plt.scatter(df[x],df[y])
        plt.ticklabel_format(style='plain', axis='y')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.show()
        plt.close()
    except Exception as e:
        print(f"Erreur dans le scatter plot: {e}")

def corr_matrix(df):
    try:
        corr = df.corr(numeric_only=True) 
        
        plt.figure(figsize=(12, 10))
        sns.heatmap(corr, 
                    annot=True,
                    fmt=".2f",
                    cmap='coolwarm',
                    vmin=-1, vmax=1,
                    center=0,
                    linewidths=.5)
        plt.title("Matrice de Corrélation")
        plt.show()
    except Exception as e:
        print(f"Erreur dans matrice de corrélation : {e}")
    
if __name__ == "__main__":
    print("Vous êtes bien dans le fichier outils_eda")