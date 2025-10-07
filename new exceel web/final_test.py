import pandas as pd

df = pd.read_excel('NOVA - COST Pricing Template  - Master2.xlsx', header=20)

required = [
    'Supplier Name', 'Factory Item Code', 'Image', 'Product Description',
    'BASIC PRODUCT SPEC', 'Unit Size', '# Units per Case/Carton:',
    'PACKAGING SPEC', 'PRODUCT SHELF LIFE', 'PRODUCT HS CODE', 'CURRENCY',
    'PRICE PER  / UNIT', 'PRICE PER  / CASE', 'INCOTERM (eg. EXW / FOB / CFR)',
    'ORIGIN', 'PORT OF LOADING', '20ft', '40ft', '40ft HQ', 'GP / REEFER',
    'PALLETISED / HANDSTACKED ', 'PALLET CONFIGURATIONS (if palletised) PER Pallet(',
    'TRUCKLOAD (LOCAL)', 'CASES PER PALLET', 'PRINTING', 'PRODUCTION', 'ORDER',
    'LENGTH (MM)', 'WIDTH (MM)', 'HEIGHT (MM)', 'WEIGHT PER CASE (KG)',
    "TI'S", "HI'S", 'PRINTING LEAD TIME', 'PRODUCTION LEAD TIME',
    'SHIPPING LEAD TIME', 'PLATE / MOULD COSTS \n(Where Applicable)', 'Certificates'
]

available = [col for col in required if col in df.columns]
filtered_df = df[available]

print(f'Total columns extracted: {len(available)}')
print(f'\nColumns in order:')
for i, col in enumerate(available, 1):
    print(f'{i}. {col}')

print(f'\n\nSample data (first row):')
print(filtered_df.iloc[0].to_dict())
