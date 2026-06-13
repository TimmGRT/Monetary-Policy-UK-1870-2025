#Ici j'essaie bien que Chat me dise que cela ne sert à rien (car cela reviens à estimer 3 modèle), de créer non seulement des dummies
# mais également de les faire interagire avec les variables de contrôle, comme on a vu en cours quoi.


import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.api import VAR

# 1. On recrée nos Dummies de base 
df_detrended['dummy_gold'] = np.where(df_detrended['year'] < 1914, 1, 0)
df_detrended['dummy_bw'] = np.where((df_detrended['year'] >= 1945) & (df_detrended['year'] <= 1971), 1, 0)
df_detrended['dummy_float'] = np.where(df_detrended['year'] > 1971, 1, 0)

variables_base = ['oil_price_stat', 'output_gap', 'cpi_stat', 'taux_directeur', 'taux_changes_stat']
variables_interagies = []

# 2. On crée la grande boucle d'interaction
# On va multiplier CHAQUE variable par CHAQUE dummy.
# On passe donc de 5 variables à 15 variables. 
for var in variables_base:
    df_detrended[f'{var}_gold'] = df_detrended[var] * df_detrended['dummy_gold']
    df_detrended[f'{var}_bw'] = df_detrended[var] * df_detrended['dummy_bw']
    df_detrended[f'{var}_float'] = df_detrended[var] * df_detrended['dummy_float']
    variables_interagies.extend([f'{var}_gold', f'{var}_bw', f'{var}_float'])

df_interact = df_detrended.set_index('year')[variables_interagies]

#Ici j'estime le modèle et génère les IRF
print("Tentative d'estimation du VAR interagi à 15 variables...")

try:
    # On estime le modèle
    res_interact = VAR(df_interact).fit(1)
    print("Succès : Le modèle a été estimé !")
    
    horizon = 10
    irf_interact = res_interact.irf(horizon)
    
    #Je génère les graphs
    noms = res_interact.names 

    # Position des chocs 
    idx_choc_gold = noms.index('taux_directeur_gold')
    idx_choc_bw = noms.index('taux_directeur_bw')
    idx_choc_float = noms.index('taux_directeur_float')

    couleurs = {'Gold': 'goldenrod', 'BW': 'steelblue', 'Float': 'crimson'}
    marqueurs = {'Gold': 'o', 'BW': 's', 'Float': '^'}
    z = 1 # Intervalle à 68%

    fig, axes = plt.subplots(nrows=len(variables_base), ncols=1, figsize=(10, 20), sharex=True)
    fig.suptitle("Impact d'un choc monétaire (Modèle Interagi à 15 variables)\nReconstitution des 3 régimes historiques", 
                 fontsize=16, fontweight='bold', y=0.98)

    # Boucle pour générer chaque graphique
    for i, var_base in enumerate(variables_base):
        ax = axes[i]
        
        idx_rep_gold = noms.index(f'{var_base}_gold')
        idx_rep_bw = noms.index(f'{var_base}_bw')
        idx_rep_float = noms.index(f'{var_base}_float')
        
        # 1. Extraction Gold
        val_g = irf_interact.orth_irfs[:, idx_rep_gold, idx_choc_gold]
        se_g = irf_interact.stderr(orth=True)[:, idx_rep_gold, idx_choc_gold]
        low_g, up_g = val_g - z * se_g, val_g + z * se_g
        
        # 2. Extraction BW
        val_bw = irf_interact.orth_irfs[:, idx_rep_bw, idx_choc_bw]
        se_bw = irf_interact.stderr(orth=True)[:, idx_rep_bw, idx_choc_bw]
        low_bw, up_bw = val_bw - z * se_bw, val_bw + z * se_bw
        
        # 3. Extraction Float
        val_f = irf_interact.orth_irfs[:, idx_rep_float, idx_choc_float]
        se_f = irf_interact.stderr(orth=True)[:, idx_rep_float, idx_choc_float]
        low_f, up_f = val_f - z * se_f, val_f + z * se_f
        
        ax.axhline(0, color='black', linewidth=1.5)
        
        # Intervalles
        ax.plot(low_g, color=couleurs['Gold'], linestyle='--', linewidth=1, alpha=0.7)
        ax.plot(up_g, color=couleurs['Gold'], linestyle='--', linewidth=1, alpha=0.7)
        ax.plot(low_bw, color=couleurs['BW'], linestyle='--', linewidth=1, alpha=0.7)
        ax.plot(up_bw, color=couleurs['BW'], linestyle='--', linewidth=1, alpha=0.7)
        ax.plot(low_f, color=couleurs['Float'], linestyle='--', linewidth=1, alpha=0.7)
        ax.plot(up_f, color=couleurs['Float'], linestyle='--', linewidth=1, alpha=0.7)
        
        # Courbes
        ax.plot(val_g, label='Étalon-Or', color=couleurs['Gold'], linewidth=2.5, marker=marqueurs['Gold'])
        ax.plot(val_bw, label='Bretton Woods', color=couleurs['BW'], linewidth=2.5, marker=marqueurs['BW'])
        ax.plot(val_f, label='Flottement', color=couleurs['Float'], linewidth=2.5, marker=marqueurs['Float'])
        
        # Esthétique
        ax.set_title(f"Réponse de : {var_base}", fontsize=12, fontweight='bold')
        ax.grid(True, linestyle='--', alpha=0.6)
        
        if i == 0:
            ax.legend(loc='upper right', fontsize=10)

    # Finitions
    plt.xlabel("Années après le choc", fontsize=12)
    plt.xticks(range(0, horizon + 1))
    plt.tight_layout()
    plt.subplots_adjust(top=0.95) 
    plt.show()

except np.linalg.LinAlgError:
    print("\nERREUR FATALE : Matrice singulière (LinAlgError).")
    print("Le modèle interagi contient trop de zéros pour que l'algorithme OLS puisse inverser la matrice.")
except Exception as e:
    print(f"\nUne autre erreur s'est produite : {e}")


couleurs  = {'Gold': 'goldenrod', 'BW': 'steelblue', 'Float': 'crimson'}
marqueurs = {'Gold': 'o',         'BW': 's',          'Float': '^'}
z = 1

for i, var_base in enumerate(variables_base):
    fig, ax = plt.subplots(figsize=(10, 4))
    fig.suptitle(f"Impact d'un choc monétaire — Réponse de : {var_base}",
                 fontsize=13, fontweight='bold')

    idx_rep_gold  = noms.index(f'{var_base}_gold')
    idx_rep_bw    = noms.index(f'{var_base}_bw')
    idx_rep_float = noms.index(f'{var_base}_float')

    # Gold
    val_g  = irf_interact.orth_irfs[:, idx_rep_gold, idx_choc_gold]
    se_g   = irf_interact.stderr(orth=True)[:, idx_rep_gold, idx_choc_gold]
    low_g, up_g = val_g - z * se_g, val_g + z * se_g

    # Bretton Woods
    val_bw  = irf_interact.orth_irfs[:, idx_rep_bw, idx_choc_bw]
    se_bw   = irf_interact.stderr(orth=True)[:, idx_rep_bw, idx_choc_bw]
    low_bw, up_bw = val_bw - z * se_bw, val_bw + z * se_bw

    # Float
    val_f  = irf_interact.orth_irfs[:, idx_rep_float, idx_choc_float]
    se_f   = irf_interact.stderr(orth=True)[:, idx_rep_float, idx_choc_float]
    low_f, up_f = val_f - z * se_f, val_f + z * se_f

    ax.axhline(0, color='black', linewidth=1.5)
    

    # Confidence bands
    for low, up, col in [(low_g, up_g, couleurs['Gold']),
                         (low_bw, up_bw, couleurs['BW']),
                         (low_f, up_f, couleurs['Float'])]:
        ax.plot(low, color=col, linestyle='--', linewidth=1, alpha=0.7)
        ax.plot(up,  color=col, linestyle='--', linewidth=1, alpha=0.7)

    # IRF lines
    ax.plot(val_g,  label='Étalon-Or',     color=couleurs['Gold'],  linewidth=2.5, marker=marqueurs['Gold'])
    ax.plot(val_bw, label='Bretton Woods', color=couleurs['BW'],    linewidth=2.5, marker=marqueurs['BW'])
    ax.plot(val_f,  label='Flottement',    color=couleurs['Float'], linewidth=2.5, marker=marqueurs['Float'])

    ax.set_xlabel("Années après le choc", fontsize=11)
    ax.set_xticks(range(0, horizon + 1))
    ax.legend(loc='upper right', fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.6)

    plt.tight_layout()
    plt.show()          # <-- closes/displays this figure before the next iteration