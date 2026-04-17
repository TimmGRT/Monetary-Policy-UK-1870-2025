import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from statsmodels.tsa.stattools import adfuller


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
def time_evo(df, column: str):
    try:
        fig = px.line(
            df, 
            x='year', 
            y=column,
            title=f"{column} evolution in time",
            labels={'year': "Year", column: "Value"},
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

import matplotlib.pyplot as plt
import seaborn as sns

def scat_period(df, x: str, y: str, xlabel: str = None, ylabel: str = None):
    try:
        def definir_periode(year):
            if 1862 <= year <= 1931:
                return '1862-1931'
            elif 1944 <= year <= 1971:
                return '1944-1971'
            elif 1972 <= year <= 2025:
                return '1972-2025'
            else:
                return 'Hors période'

        df_plot = df.copy()
        df_plot['Periode'] = df_plot['year'].apply(definir_periode)
        df_plot = df_plot[df_plot['Periode'] != 'Hors période']

        plt.figure(figsize=(10, 7))
        
        order = ['1862-1931', '1944-1971', '1972-2025']
        
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
        
        # MODIFICATION : Utilise les labels personnalisés ou les noms de colonnes par défaut
        plt.xlabel(xlabel if xlabel else x)
        plt.ylabel(ylabel if ylabel else y)
        
        plt.legend(title="Periods")
        plt.grid(True, linestyle=':', alpha=0.6)
        
        plt.show()
        plt.close()

    except Exception as e:
        print(f"Erreur dans le scatter plot : {e}")

### affiche les matrices de corrélation du df en ignorant la colonne année pour chaque périodes distinctes 
def corr_matrix(df):
    # Mise à jour de la première période à 1864
    periodes = [
        (1871, 1914, "1871-1914"),
        (1945, 1971, "1944-1971"),
        (1972, 2025, "1972-2025")
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
            
            plt.title(f"Correlation matrix : {titre}")
            plt.show()
            plt.close()
            
        except Exception as e:
            print(f"Erreur lors du calcul pour la {titre} : {e}")

### affiche la matrice de corrélation incluant les lags pour comprendre la corrélation entre les différentes temps t et choisir les bons lags.
### target col est la colonne en temps t et feature col est la colonne en temps t, t-1, t-2 etc jusqu'à t-5
def plot_future_impact_heatmap(df, cause_col, effect_col, max_leads=5):
    lead_data = pd.DataFrame()

    lead_data[cause_col] = df[cause_col]

    for i in range(0, max_leads + 1):
        lead_data[f'{effect_col}_{i}y'] = df[effect_col].shift(-i)

    corr_matrix = lead_data.corr()

    heatmap_data = corr_matrix[[cause_col]].drop(index=cause_col).T
    
    plt.figure(figsize=(15, 3))
    sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', center=0, fmt=".2f", cbar=False)
    
    plt.title(f"Impact of today's {cause_col} on {effect_col} future")
    plt.xlabel("Time horizon")
    plt.show()
    plt.close()


# Calcule ce qu'on appelle les corrélations roulantes et les plot dans un graph (plus d'explications dans mon fichier eda)
def plot_rolling_corr(df, x_col, y_cols, window=20):
    try:
        df_sorted = df.sort_values('year')
        fig = go.Figure()

        for y_col in y_cols:
            rolling_corr = df_sorted[x_col].rolling(window=window, min_periods=window//2).corr(df_sorted[y_col])
            
            fig.add_trace(go.Scatter(
                x=df_sorted['year'], 
                y=rolling_corr,
                mode='lines',
                name=f"Corr({x_col} / {y_col})",
                hovertemplate="Année: %{x}<br>Corrélation: %{y:.2f}<extra></extra>"
            ))

        fig.update_layout(
            title=f"Impact of {x_col} on the Economy ({window}-Year Rolling Correlations)",
            xaxis_title="Year",
            yaxis_title="Correlation coefficient",
            yaxis=dict(range=[-1.1, 1.1]),
            template="plotly_white",
            
            height=500, 
            width=900,
            legend=dict(
                orientation="v",
                yanchor="top", 
                y=1,
                xanchor="left", 
                x=1.02
            ),
            margin=dict(r=150)
        )

        fig.add_hline(y=0, line_dash="dash", line_color="black", opacity=0.5)

        fig.show()
    except Exception as e:
        print(f"Erreur dans le graphique combiné : {e}")

# Cette fonction nous permet de faire un test ADF sur les données d'un dataframe "df" en enlevant la variable "year"
def check_stationarity(df):
    results = []
    # On filtre pour ne garder que les colonnes numériques et exclure 'year'
    cols_to_test = [c for c in df.select_dtypes(include=['number']).columns if c.lower() != 'year']
    
    for col in cols_to_test:
        try:
            # On retire les valeurs manquantes (le test ADF ne les accepte pas)
            series = df[col].dropna()
            
            if len(series) < 20:
                continue

            res = adfuller(series)
            p_val = res[1]
            
            is_stationary = p_val < 0.05
            
            results.append({
                'Variable': col,
                'p-value': round(p_val, 4),
                'Stationnaire': "OUI" if is_stationary else "NON -> à stationariser"
            })
        except Exception as e:
            results.append({'Variable': col, 'p-value': "Erreur", 'Stationnaire': str(e)})
            
    results_df = pd.DataFrame(results)

    return results_df

### Cette fonction permet de stationnariser les colonnes séléctionnées d'un dataframe "df" avec soit la méthode des simples différences (par défaut) soit la méthode des logs (si l'on mentionne "log")
def stationnarize(df, columns_to_diff, method = 'simple'):
    df_stat = df.copy()
    for col in columns_to_diff:
        if method == 'log':
            df_stat[f'{col}_stat'] = np.log(df_stat[col] + 1e-6).diff() # on rajoute une toute petit constante pour ne pas avoir l'ereur venant de log(0=
        elif method == 'simple':
            df_stat[f'{col}_stat'] = df_stat[col].diff()
            
    return df_stat

def time_evo_clean(df, columns: list, save_path=None):
    try:
        if isinstance(columns, str):
            columns = [columns]
            
        fig = px.line(
            df, 
            x='year', 
            y=columns,
            title=None, # Pas de titre
            labels={'year': "Year", 'value': "Value"}, # Titres des axes
            template="plotly_white"
        )

        fig.update_layout(
            showlegend=False,        # MODIFICATION : Supprime la légende (description)
            xaxis_tickformat='d', 
            yaxis_tickformat='.2f',
            margin=dict(t=10, b=10, l=10, r=10) # Réduit les marges blanches autour
        )

        # Désactive le petit graph de sélection en dessous
        fig.update_xaxes(rangeslider_visible=False)

        fig.show()

        if save_path:
            fig.write_image(save_path)
            print(f"Graphique minimaliste sauvegardé : {save_path}")

    except Exception as e: 
        print(f"Erreur : {e}")
    
if __name__ == "__main__":
    print("Vous êtes bien dans le fichier outils_eda")