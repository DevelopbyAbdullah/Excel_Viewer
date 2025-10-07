import pandas as pd

df = pd.read_excel('NOVA - COST Pricing Template  - Master2.xlsx', header=20)

# Excel columns (skip first Unnamed column)
excel_cols = [col for col in df.columns if not col.startswith('Unnamed')]

# Required columns from app.py
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

print('Excel Order vs Required Order:')
print('='*80)
for i, (excel_col, req_col) in enumerate(zip(excel_cols, required), 1):
    match = 'OK' if excel_col == req_col else 'MISMATCH'
    print(f'{i}. [{match}]')
    print(f'   Excel:    "{excel_col}"')
    print(f'   Required: "{req_col}"')
    if excel_col != req_col:
        print(f'   >>> DIFFERENCE FOUND!')
    print()
