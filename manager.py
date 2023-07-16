import os
import pandas as pd

# Cleans the terminal
def ct():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to get the path of the script
def get_path():
    return os.path.dirname(os.path.abspath(__file__))

# Cleans the terminal
ct()

# Gets the directory where the script is
path = get_path()

# Opens a txt file with the necessary info
with open('database.txt', 'r', encoding='utf-8') as file:
    info = file.readlines()
    dado = ' '.join(info)
    items = dado.split(',')

    values = []

# Loop through the file contents to extract data
for i in range(1, len(info)):
    x = 5 * (i - 1)
    data = items[0 + x].strip()
    tipo = items[1 + x].strip()
    categoria = items[2 + x].strip()
    metodo = items[3 + x].strip()
    valor = items[4 + x].strip()
    values.append([data, tipo, categoria, metodo, valor])
 
# Create a DataFrame from the extracted values
df = pd.DataFrame(values, columns=["DATA", "TIPO", "CATEGORIA", "MÉTODO", "VALOR"])

# Convert 'VALOR' column to numeric type
df['VALOR'] = pd.to_numeric(df['VALOR'])

# Function to calculate extra information
def extra_infos():
    # Filter receitas (revenues) and despesas (expenses) separately
    receitas = df[df['TIPO'] == 'r'].copy()
    receitas_total = receitas['VALOR'].sum()
    despesas = df[df['TIPO'] == 'd'].copy()
    despesas_total = despesas['VALOR'].sum()
    
    # Convert 'VALOR' column to numeric type
    despesas['VALOR'] = pd.to_numeric(despesas['VALOR'])
    receitas['VALOR'] = pd.to_numeric(receitas['VALOR'])
    
    # Calculate totals by MÉTODO (method)
    despesas_met = despesas.groupby('MÉTODO')['VALOR'].sum()
    receitas_met = receitas.groupby('MÉTODO')['VALOR'].sum()
    
    # Calculate totals by CATEGORIA (category)
    despesas_cat = despesas.groupby('CATEGORIA')['VALOR'].sum()
    receitas_cat = receitas.groupby('CATEGORIA')['VALOR'].sum()
    
    # Calculate surplus/deficit
    supv = receitas_total - despesas_total
    
    # Calculate percentage of expenses to revenues
    percD_R = (despesas_total / receitas_total) * 100 if receitas_total != 0 else 0
    
    # Calculate expense percentages by method
    percD_M = (despesas_met / despesas_total) * 100 if despesas_total != 0 else 0

    # Calculate expense percentages by category
    percD_C = (despesas_cat / despesas_total) * 100 if despesas_total != 0 else 0

    # Calculate revenue percentages by method
    percR_M = (receitas_met / receitas_total) * 100 if receitas_total != 0 else 0

    # Calculate revenue percentages by category
    percR_C = (receitas_cat / receitas_total) * 100 if receitas_total != 0 else 0
    
    # Convert 'DATA' columns to datetime format
    df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y')
    receitas['DATA'] = pd.to_datetime(receitas['DATA'], format='%d/%m/%Y')
    despesas['DATA'] = pd.to_datetime(despesas['DATA'], format='%d/%m/%Y')
    
    # Calculate date-related information
    data_min = df['DATA'].min()
    data_max = df['DATA'].max()
    
    periodo = data_max - data_min
    anos = periodo.days // 365
    meses = (periodo.days % 365) // 30
    dias = (periodo.days % 365) % 30
    
    def formatar_periodo(anos, meses, dias):
        # Format the period string
        periodo_str = ''

        if anos > 0:
            periodo_str += f'{anos} ano' if anos == 1 else f'{anos} anos'

        if meses > 0:
            periodo_str += f', {meses} mês' if meses == 1 else f' {meses} meses'

        if dias > 0:
            periodo_str += f' e {dias} dia' if dias == 1 else f' e {dias} dias'

        if not periodo_str:
            periodo_str = '0 dias'
        return periodo_str
        
    periodo_str = formatar_periodo(anos, meses, dias)

    # Calculate average daily expenses and revenues
    mdia_d_D = (despesas_total / dias) if dias != 0 else 0
    mdia_r_D = (receitas_total / dias) if dias != 0 else 0
    
    # Add columns with total despesas and receitas to respective DataFrames
    receitas['TOTAL'] = receitas_total
    receitas.loc[1:, 'TOTAL'] = pd.NA
    despesas['TOTAL'] = despesas_total
    despesas.loc[2:, 'TOTAL'] = pd.NA
    
    # Return the calculated values 
    return receitas, receitas_total, receitas_met, receitas_cat, despesas, despesas_total, despesas_met, despesas_cat, supv, percD_R, percD_M, percD_C, percR_M, percR_C, data_min, data_max, periodo, periodo_str, mdia_d_D, mdia_r_D

# Save the data to an Excel file
with pd.ExcelWriter("infos.xlsx") as writer:
    # Save receitas (revenues) DataFrame to 'receitas' sheet
    receitas_df = extra_infos()[0]
    receitas_df['DATA'] = receitas_df['DATA'].dt.strftime('%d/%m/%Y')
    receitas_df.drop(columns=['TIPO']).to_excel(writer, index=False, sheet_name="receitas")
    
    # Save despesas (expenses) DataFrame to 'despesas' sheet
    despesas_df = extra_infos()[4]
    despesas_df['DATA'] = despesas_df['DATA'].dt.strftime('%d/%m/%Y')
    despesas_df.drop(columns=['TIPO']).to_excel(writer, index=False, sheet_name="despesas")
