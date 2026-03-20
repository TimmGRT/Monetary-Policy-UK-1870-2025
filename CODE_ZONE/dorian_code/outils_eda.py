import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px


### créé un histogramme pour le dataframe "df" et la colonne que vous souhaitez, attention, fonctionne seulement si vous utilisez le df qui vient de "main_cleaned.parquet" car la fonction récupère "year"
def histogram(df, column: str):
    try:
        fig = px.histogram(
            df, 
            x=column, 
            nbins=20,
            title=f"Distribution de {column}",
            labels={column: "Valeur", "count": "Nombre d'occurrences"},
            template="plotly_white",
            color_discrete_sequence=['#636EFA']
        )
        fig.update_layout(
            bargap=0.1,
            xaxis_tickformat='d'
        )
        fig.show()
    except Exception as e: 
        print(f"Erreur dans l'histogramme : {e}")

### créé un graphique d'évolution dans le temps de la variable column qui se trouve dans le dataframe "df"
import plotly.express as px

def time_evo(df, column: str):
    try:
        fig = px.line(
            df, 
            x='year', 
            y=column,
            title=f"Évolution de {column} au cours du temps",
            labels={'year': "Année", column: "Valeur"},
            markers=True,         # Ajoute des points sur la ligne pour chaque donnée
            template="plotly_white"
        )

        fig.update_layout(
            xaxis_tickformat='d', 
            yaxis_tickformat='.2f'
        )

        fig.update_xaxes(rangeslider_visible=True)

        fig.show()
    except Exception as e: 
        print(f"Erreur dans le graphique d'évolution : {e}")

### créé un scatter plot pour les variables x et y du dataframe "df" pour chaque période distincte
def scat_period(df, x: str, y: str):
    try:
        def definir_periode(year):
            if 1850 <= year <= 1931:
                return '1850-1931'
            elif 1944 <= year <= 1971:
                return '1944-1971'
            elif 1972 <= year <= 2025:
                return '1972-2025'
            else:
                return 'Hors période' # Pour les années comme 1935, 1940, etc.

        df_plot = df.copy()
        df_plot['Periode'] = df_plot['year'].apply(definir_periode)

        df_plot = df_plot[df_plot['Periode'] != 'Hors période']

        plt.figure(figsize=(10, 7))
        
        order = ['1850-1931', '1944-1971', '1972-2025']
        
        sns.scatterplot(
            data=df_plot, 
            x=x, 
            y=y, 
            hue='Periode', 
            hue_order=order,
            palette='bright', 
            s=80, 
            edgecolor='w', 
            alpha=0.7
        )

        plt.ticklabel_format(style='plain', axis='both')
        plt.title(f"Analyse par périodes spécifiques : {x} vs {y}")
        plt.xlabel(x)
        plt.ylabel(y)
        plt.legend(title="Périodes")
        plt.grid(True, linestyle=':', alpha=0.6)
        
        plt.show()
        plt.close()

    except Exception as e:
        print(f"Erreur dans le scatter plot : {e}")

### affiche les matrices de corrélation du df en ignorant la colonne année pour chaque périodes distinctes 
def corr_matrix(df):
    periodes = [
        (1850, 1931, "Période 1850-1931"),
        (1944, 1971, "Période 1944-1971"),
        (1972, 2025, "Période 1972-2025")
    ]
    
    for debut, fin, titre in periodes:
        try:
            df_periode = df[(df['year'] >= debut) & (df['year'] <= fin)]

            df_filtered = df_periode.drop(columns=['year'], errors='ignore')
            corr = df_filtered.corr(numeric_only=True)
            
            plt.figure(figsize=(10, 7))
            sns.heatmap(corr, 
                        annot=True,
                        fmt=".2f",
                        cmap='coolwarm',
                        vmin=-1, vmax=1,
                        center=0,
                        linewidths=.5)
            
            plt.title(f"Matrice de Corrélation : {titre}")
            plt.show()
            plt.close()
            
        except Exception as e:
            print(f"Erreur lors du calcul pour la {titre} : {e}")
    
if __name__ == "__main__":
    print("Vous êtes bien dans le fichier outils_eda")