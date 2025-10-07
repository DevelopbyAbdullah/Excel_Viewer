import pandas as pd

df = pd.read_excel('NOVA - COST Pricing Template  - Master2.xlsx', header=20)

print('Excel file ke columns (order mein):')
print('='*60)
for i, col in enumerate(df.columns, 1):
    print(f'{i}. {col}')

print('\n\nRequired columns list:')
print('='*60)
required = [
    'Supplier Name', 'Factory Item Code', 'Image', 'Product Description',
    'BASIC PRODUCT SPEC', 'Unit Size', '# Units per Case/Carton:',
    'PACKAGING SPEC', 'PRODUCT SHELF LIFE', 'PRODUCT HS CODE', 'CURRENCY',
    'PRICE PER  / UNIT', 'PRICE PER  / CASE', 'INCOTERM (eg. EXW / FOB / CFR)',
    'ORIGIN', 'PORT OF LOADING', '20ft', '40ft', '40ft HQ', 'GP / REEFER',
    'PALLETISED / HANDSTACKED', 'PALLET CONFIGURATIONS (if palletised) PER Pallet(',
    'TRUCKLOAD (LOCAL)', 'CASES PER PALLET', 'PRINTING', 'PRODUCTION', 'ORDER',
    'LENGTH (MM)', 'WIDTH (MM)', 'HEIGHT (MM)', 'WEIGHT PER CASE (KG)',
    "TI'S", "HI'S", 'PRINTING LEAD TIME', 'PRODUCTION LEAD TIME',
    'SHIPPING LEAD TIME', '"PLATE / MOULD COSTS \n(Where Applicable)"', 'Certificates'
]

for i, col in enumerate(required, 1):
    exists = col in df.columns
    print(f'{i}. {col} - {"FOUND" if exists else "NOT FOUND"}')
