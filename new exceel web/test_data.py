import pandas as pd

# Read with correct header
df = pd.read_excel('NOVA - COST Pricing Template  - Master2.xlsx', header=20)

print(f'Total Rows: {len(df)}')
print(f'\nColumns found: {len(df.columns)}')
print('\nFirst 5 column names:')
for i, col in enumerate(df.columns[:5]):
    print(f'{i+1}. {col}')

print('\n\nFirst 2 data rows:')
print(df.head(2)[['Supplier Name', 'Factory Item Code', 'Product Description']].to_string())

# Check which required columns exist
required = ['Supplier Name', 'Factory Item Code', 'Image', 'Product Description', 
            'BASIC PRODUCT SPEC', 'Unit Size', '# Units per Case/Carton:']
print('\n\nChecking required columns:')
for col in required:
    exists = col in df.columns
    print(f'{col}: {"YES" if exists else "NO"}')
