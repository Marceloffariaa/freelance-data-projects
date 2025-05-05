from data_merge_pipeline_class import DataHandler
import os

# Define input file paths
path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

# Create output folder if not exists
os.makedirs('data_processed', exist_ok=True)

# EXTRACT
company_a = DataHandler(path_json, 'json')
print("Company A columns:", company_a.columns)
print("Company A rows:", company_a.num_rows)

company_b = DataHandler(path_csv, 'csv')
print("Company B columns:", company_b.columns)
print("Company B rows:", company_b.num_rows)

# TRANSFORM
column_mapping = {
    'Nome do Item': 'Product Name',
    'Classificação do Produto': 'Product Category',
    'Valor em Reais (R$)': 'Product Price (R$)',
    'Quantidade em Estoque': 'Stock Quantity',
    'Nome da Loja': 'Store',
    'Data da Venda': 'Sale Date'
}

company_b.rename_columns(column_mapping)
print("Company B renamed columns:", company_b.columns)

# JOIN
merged_data = DataHandler.join(company_a, company_b)
print("Merged columns:", merged_data.columns)
print("Merged rows:", merged_data.num_rows)

# LOAD
output_path = 'data_processed/merged_data.csv'
merged_data.save_to_csv(output_path)
print("Merged data saved at:", output_path)
