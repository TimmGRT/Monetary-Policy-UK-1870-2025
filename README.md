# Monetary Policy Transmission in the UK across Monetary Regimes (1870–2025)

**Research question:** how does the effectiveness of UK monetary-policy shocks on output, inflation and the exchange rate change across the **Gold Standard**, **Bretton Woods** and **floating exchange rate** regimes?

Empirical macroeconomics project for the course *Recherche empirique en économie*, HEC Lausanne (2026). The project was graded **6/6**.

## Methodology

| Step | Method | Location |
|---|---|---|
| Data pipeline | Long-run UK macro series, cleaned and detrended, stored as Parquet | `DATALAKE/` |
| Cycle extraction | Hodrick–Prescott and Hamilton (2018) filters | `CODE_ZONE/timeo_code/` |
| Exploratory analysis | Rolling correlations, lagged cross-correlation heatmaps by regime | `CODE_ZONE/dorian_code/` |
| Baseline | OLS regressions of output gap, inflation and exchange rate on policy-rate changes, by regime | `CODE_ZONE/veljko_code/` |
| Identification | Structural VAR, impulse responses to a policy-rate shock | `CODE_ZONE/ryan_code/` |
| Regime dependence | Markov-switching regressions and MS-VAR on output, inflation and the exchange rate | `CODE_ZONE/timeo_code/` |

## Repository layout

```
DATALAKE/            shared data layer (data.py, cleaned + detrended parquet files)
CODE_ZONE/
  timeo_code/        filters, Markov-switching and MS-VAR models, final regime plots
  ryan_code/         SVAR
  veljko_code/       OLS tables (LaTeX output)
  dorian_code/       exploratory analysis and figures
```

## Reproduce

```bash
git clone https://github.com/TimmGRT/Monetary-Policy-UK-1870-2025.git
cd Monetary-Policy-UK-1870-2025
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

## Team

Timéo Grienti · Dorian · Ryan · Veljko
