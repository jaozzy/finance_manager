from essencials import ct, get_path
import matplotlib.pyplot as plt
from manager import extra_infos as extra
import pandas as pd
import os
import shutil

ct()

# Obtém as informações extras do manager.py
receitas, receitas_total, receitas_met, receitas_cat, despesas, despesas_total, despesas_met, despesas_cat, supv, percD_R, percD_M, percD_C, percR_M, percR_C, data_min, data_max, periodo, periodo_str, mdia_d_D, mdia_r_D = extra()

# Lista para armazenar os percentuais das despesas em relação às categorias
percentuais_d_cat = []
d_cats = []

# Cálculo dos percentuais das despesas em relação às categorias
for cat, despesa in despesas_cat.items():
    percentuais_d_cat.append((despesa / despesas_total) * 100)
    d_cats.append(cat.upper())

# Plotagem do gráfico de despesas em relação às categorias
fig, ax = plt.subplots()
wedges, labels, autotexts = ax.pie(percentuais_d_cat, autopct='', startangle=90)
ax.axis('equal')

# Configuração da legenda
legend_labels = [f'{label}: {percentual:.2f}%' for label, percentual in zip(d_cats, percentuais_d_cat)]
ax.legend(wedges, legend_labels, loc='center left', bbox_to_anchor=(1.3, 0.5), title='Categorias')

#
fig.subplots_adjust(left=0.5)

# Salva o gráfico de despesas em relação às categorias
fig.savefig('grafico_despesas_categoria.png', bbox_inches='tight')

# Lista para armazenar os percentuais das despesas em relação aos métodos
percentuais_d_metodo = []
d_metodos = []

# Cálculo dos percentuais das despesas em relação aos métodos
for metodo, despesa in despesas_met.items():
    percentuais_d_metodo.append((despesa / despesas_total) * 100)
    d_metodos.append(metodo.upper())

# Plotagem do gráfico de métodos
fig2, ax2 = plt.subplots()
wedges, labels, autotexts = ax2.pie(percentuais_d_metodo, autopct='', startangle=90)
ax2.axis('equal')

#
fig2.subplots_adjust(left=0.5)

# Configuração da legenda
legend_labels = [f'{label}: {percentual:.2f}%' for label, percentual in zip(d_metodos, percentuais_d_metodo)]
ax2.legend(wedges, legend_labels, loc='center left', bbox_to_anchor=(1.3, 0.5), title='Métodos')

# Salva o gráfico de métodos
fig2.savefig('grafico_despesas_metodo.png', bbox_inches='tight')

# Lista para armazenar os percentuais das receitas em relação às categorias
percentuais_r_cat = []
r_cats = []

# Cálculo dos percentuais das receitas em relação às categorias
for categoria, receita in receitas_cat.items():
    percentuais_r_cat.append((receita / receitas_total) * 100)
    r_cats.append(categoria.upper())

# Plotagem do gráfico de receitas em relação às categorias
fig3, ax3 = plt.subplots()
wedges, labels, autotexts = ax3.pie(percentuais_r_cat, autopct='', startangle=90)
ax3.axis('equal')

#
fig3.subplots_adjust(left=0.5)

# Configuração da legenda
legend_labels = [f'{label}: {percentual:.2f}%' for label, percentual in zip(r_cats, percentuais_r_cat)]
ax3.legend(wedges, legend_labels, loc='center left', bbox_to_anchor=(1.3, 0.5), title='Categorias')

# Salva o gráfico de receitas em relação às categorias
fig3.savefig('grafico_receitas_categoria.png', bbox_inches='tight')

# Lista para armazenar os percentuais das receitas em relação aos métodos
percentuais_r_metodo = []
r_metodos = []

# Cálculo dos percentuais das receitas em relação aos métodos
for metodo, receita in receitas_met.items():
    percentuais_r_metodo.append((receita / receitas_total) * 100)
    r_metodos.append(metodo.upper())

# Plotagem do gráfico de receitas em relação aos métodos
fig4, ax4 = plt.subplots()
wedges, labels, autotexts = ax4.pie(percentuais_r_metodo, autopct='', startangle=90)
ax4.axis('equal')

#
fig4.subplots_adjust(left=0.5)

# Configuração da legenda
legend_labels = [f'{label}: {percentual:.2f}%' for label, percentual in zip(r_metodos, percentuais_r_metodo)]
ax4.legend(wedges, legend_labels, loc='center left', bbox_to_anchor=(1.3, 0.5), title='Métodos')

# Salva o gráfico de receitas em relação aos métodos
fig4.savefig('grafico_receitas_metodo.png', bbox_inches='tight')

# Move os arquivos de gráfico para a pasta 'graphs'
path = get_path()
files = os.listdir(path)
dest = f'{path}/graphs/'

for file in files:
    if file.endswith('.png'):
        shutil.move(file, dest)

print('Gráficos gerados com sucesso')
