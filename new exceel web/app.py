from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create uploads directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Global variable to store the current dataframe
current_df = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    global current_df
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file selected'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'})
    
    if file and file.filename.endswith(('.xlsx', '.xls')):
        try:
            # Read Excel file directly from memory with header on row 20
            current_df = pd.read_excel(file, header=20)
            
            # Clean column names - convert to string and handle NaN
            current_df.columns = [str(col) if pd.notna(col) else f'Column_{i}' for i, col in enumerate(current_df.columns)]
            
            total_rows = len(current_df)
            
            return jsonify({
                'success': True,
                'message': f'File uploaded successfully! {total_rows} rows found.'
            })
        except Exception as e:
            return jsonify({'error': f'Error reading file: {str(e)}'})
    
    return jsonify({'error': 'Please upload a valid Excel file (.xlsx or .xls)'})

# Define required columns (exact match from Excel)
REQUIRED_COLUMNS = [
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

@app.route('/search', methods=['POST'])
def search_data():
    global current_df
    
    if current_df is None:
        return jsonify({'error': 'Please upload an Excel file first'})
    
    search_term = request.json.get('search_term', '').strip()
    
    if not search_term:
        return jsonify({'error': 'Please enter a search term'})
    
    if len(search_term) < 2:
        return jsonify({'message': 'Type at least 2 characters to search', 'data': []})
    
    try:
        # Filter only required columns that exist in the dataframe
        available_cols = [col for col in REQUIRED_COLUMNS if col in current_df.columns]
        filtered_df = current_df[available_cols]
        
        # Perform case-insensitive search across filtered columns
        mask = pd.Series([False] * len(filtered_df))
        
        for col in available_cols:
            mask |= filtered_df[col].astype(str).str.contains(search_term, case=False, na=False)
        
        results = filtered_df[mask]
        
        if results.empty:
            return jsonify({'message': 'No results found', 'data': []})
        
        # Limit results for better performance (show top 100 results)
        total_results = len(results)
        if total_results > 100:
            results = results.head(100)
            message = f'Showing top 100 of {total_results} results'
        else:
            message = f'Found {total_results} results'
        
        # Convert results to list of dictionaries and handle NaN values
        results_list = results.fillna('').to_dict('records')
        
        return jsonify({
            'success': True,
            'message': message,
            'data': results_list,
            'columns': available_cols
        })
        
    except Exception as e:
        return jsonify({'error': f'Search error: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)