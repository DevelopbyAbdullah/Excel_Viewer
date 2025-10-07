import pandas as pd

# Test different header rows
for i in range(5):
    print(f"\n=== Testing header={i} ===")
    try:
        df = pd.read_excel('NOVA - COST Pricing Template  - Master2.xlsx', header=i)
        print(f"Columns: {df.columns.tolist()[:10]}")
        print(f"First row: {df.iloc[0].tolist()[:5]}")
    except Exception as e:
        print(f"Error: {e}")
