import pandas as pd

# Load the main Excel file
SOURCE_FILE = '24 junio.xlsx'
xl = pd.ExcelFile(SOURCE_FILE)

# Assume the first sheet contains the data
sheet = xl.sheet_names[0]
df = xl.parse(sheet)

# Remove total rows
mask_totals = df[df.columns[0]].astype(str).str.contains('Total', na=False)
df = df[~mask_totals]

# Identify cost and price rows
cost_rows = df[df['COSTO/VENTA'] == 0]
price_rows = df[df['COSTO/VENTA'] == 1]

# Prepare cost data for SKU pivot
cols = ['Nombre Producto', 'Sigla de laboratorio', 'Código de Producto']
cost = cost_rows[cols].copy()

# Prepare price data for price pivot
def final_price_column(dataframe):
    """Return the last numeric column name."""
    for col in reversed(dataframe.columns):
        if pd.api.types.is_numeric_dtype(dataframe[col]):
            return col
    return dataframe.columns[-1]

price_col = final_price_column(df)
price = price_rows[['Nombre Producto', 'Sigla de laboratorio', price_col]].copy()
price.rename(columns={price_col: 'Precio'}, inplace=True)

# Pivot SKUs per lab
sku_pivot = cost.pivot_table(index='Nombre Producto',
                             columns='Sigla de laboratorio',
                             values='Código de Producto',
                             aggfunc='first')
sku_pivot.reset_index(inplace=True)

# Pivot prices per lab
price_pivot = price.pivot_table(index='Nombre Producto',
                                columns='Sigla de laboratorio',
                                values='Precio',
                                aggfunc='first')
price_pivot.reset_index(inplace=True)

# Save to CSV files
sku_pivot.to_csv('lab_products_sku.csv', index=False)
price_pivot.to_csv('lab_products_precio.csv', index=False)
print('CSV files generated: lab_products_sku.csv, lab_products_precio.csv')
