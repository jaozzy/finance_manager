from essencials import ct, get_path
import matplotlib.pyplot as plt
from manager import extra_infos as extra
import pandas as pd
import os
import shutil

ct()

path = get_path()

# Obtém as informações extras do manager.py
receitas, receitas_total, receitas_met, despesas, despesas_total, despesas_met, supv, percD_R, data_min, data_max, periodo, periodo_str, mdia_d_D, mdia_r_D = extra()

# Lista para armazenar os percentuais das categorias
percentuais_cat = []
cats = []

# Cálculo dos percentuais das categorias
for cat, gasto in gcat.items():
    gperccat = (gasto / gastos_total) * 100
    percentuais_cat.append(gperccat)
    cats.append(cat.upper())

# Plotagem do gráfico de categorias
fig, ax = plt.subplots()
ax.pie(percentuais_cat, labels=cats, autopct='%1.2f%%', startangle=90)
ax.axis('equal')

# Salva o gráfico de categorias
fig.savefig('grafico_categoria.png')

# Lista para armazenar os percentuais dos métodos
percentuais_metodo = []
metodos = []

'''
# Cálculo dos percentuais dos métodos
for metodo, gasto in gmet.items():
    gpercmet = (gasto / gastos_total) * 100
    percentuais_metodo.append(gpercmet)
    metodos.append(metodo.upper())

# Plotagem do gráfico de métodos
fig2, ax2 = plt.subplots()
ax2.pie(percentuais_metodo, labels=metodos, autopct='%1.2f%%', startangle=90)
ax2.axis('equal')

# Salva o gráfico de métodos
fig2.savefig('grafico_metodo.png')
'''

# Move os arquivos de gráfico para a pasta 'graphs'
files = os.listdir()
dest = f'{path}/graphs/'

for file in files:
    if file.endswith('.png'):
        shutil.move(file, dest)

print('Gráficos gerados com sucesso!')