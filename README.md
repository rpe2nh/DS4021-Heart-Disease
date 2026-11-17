# DS 4021: Predicting Heart Disease

**Group:** Mark Espiritu, Alicia Yoo, Esther Yun
**Course:** DS 4021, Fall 2026

## Research question
To what extent can patient demographic and clinical characteristics, such as age, blood pressure, cholesterol levels, and heart rate, predict the presence of heart disease?

## Data
UCI Heart Disease dataset (Cleveland subset, 303 samples, 13 features): https://archive.ics.uci.edu/dataset/45/heart+disease

- `Data/development_set.csv`: 80% of the data (242 rows), used for all exploration, tuning, and model building.
- `Data/reporting_set.csv`: 20% held-out reporting set (61 rows). **Do not open, analyze, or use for tuning until the final phase.**
- `split_data.py`: script used to create the split (seed 4021, stratified on heart disease status).
