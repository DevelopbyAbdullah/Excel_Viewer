import pandas as pd

df = pd.read_excel('NOVA - COST Pricing Template  - Master2.xlsx', header=None)

for i in range(15, 25):
    print(f'\nRow {i}:')
    print(df.iloc[i, 0:10].tolist())
