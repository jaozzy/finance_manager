import os
import shutil
import matplotlib.pyplot as plt
from manager import extra_infos as extra
from essencials import ct, get_path, start_py_file, del_file

ct()

path = get_path()
dest = f'{path}/graphs/'

# List of graph file names
graphnames = ['grafico_despesas_categoria.png', 'grafico_despesas_metodo.png', 'grafico_receitas_categoria.png', 'grafico_receitas_metodo.png']

for graph in graphnames:
    # Call the del_file function to delete the old graph file
    del_file(f'{dest}/{graph}')


# Get extra information from manager.py
receitas, receitas_total, receitas_met, receitas_cat, despesas, despesas_total, despesas_met, despesas_cat, supv, percD_R, percD_M, percD_C, percR_M, percR_C, data_min, data_max, periodo, periodo_str, mdia_d_D, mdia_r_D = extra()

# List to store the percentage of expenses per category
percentuais_d_cat = []
d_cats = []

# Calculate the percentage of expenses per category
for cat, despesa in despesas_cat.items():
    percentuais_d_cat.append((despesa / despesas_total) * 100)
    d_cats.append(cat.upper())

# Plot the expense chart per category
fig, ax = plt.subplots()
wedges, labels, autotexts = ax.pie(percentuais_d_cat, autopct='', startangle=90)
ax.axis('equal')

# Configure the legend
legend_labels = [f'{label}: {percentual:.2f}%' for label, percentual in zip(d_cats, percentuais_d_cat)]
ax.legend(wedges, legend_labels, loc='center left', bbox_to_anchor=(1.3, 0.5), title='Categories')

# Adjust the position of the chart
fig.subplots_adjust(left=0.5)

# Save the expense chart per category
fig.savefig('grafico_despesas_categoria.png', bbox_inches='tight')

# List to store the percentage of expenses per method
percentuais_d_metodo = []
d_metodos = []

# Calculate the percentage of expenses per method
for metodo, despesa in despesas_met.items():
    percentuais_d_metodo.append((despesa / despesas_total) * 100)
    d_metodos.append(metodo.upper())

# Plot the method chart
fig2, ax2 = plt.subplots()
wedges, labels, autotexts = ax2.pie(percentuais_d_metodo, autopct='', startangle=90)
ax2.axis('equal')

# Adjust the position of the chart
fig2.subplots_adjust(left=0.5)

# Configure the legend
legend_labels = [f'{label}: {percentual:.2f}%' for label, percentual in zip(d_metodos, percentuais_d_metodo)]
ax2.legend(wedges, legend_labels, loc='center left', bbox_to_anchor=(1.3, 0.5), title='Methods')

# Save the method chart
fig2.savefig('grafico_despesas_metodo.png', bbox_inches='tight')

# List to store the percentage of revenue per category
percentuais_r_cat = []
r_cats = []

# Calculate the percentage of revenue per category
for categoria, receita in receitas_cat.items():
    percentuais_r_cat.append((receita / receitas_total) * 100)
    r_cats.append(categoria.upper())

# Plot the revenue chart per category
fig3, ax3 = plt.subplots()
wedges, labels, autotexts = ax3.pie(percentuais_r_cat, autopct='', startangle=90)
ax3.axis('equal')

# Adjust the position of the chart
fig3.subplots_adjust(left=0.5)

# Configure the legend
legend_labels = [f'{label}: {percentual:.2f}%' for label, percentual in zip(r_cats, percentuais_r_cat)]
ax3.legend(wedges, legend_labels, loc='center left', bbox_to_anchor=(1.3, 0.5), title='Categories')

# Save the revenue chart per category
fig3.savefig('grafico_receitas_categoria.png', bbox_inches='tight')

# List to store the percentage of revenue per method
percentuais_r_metodo = []
r_metodos = []

# Calculate the percentage of revenue per method
for metodo, receita in receitas_met.items():
    percentuais_r_metodo.append((receita / receitas_total) * 100)
    r_metodos.append(metodo.upper())

# Plot the revenue chart per method
fig4, ax4 = plt.subplots()
wedges, labels, autotexts = ax4.pie(percentuais_r_metodo, autopct='', startangle=90)
ax4.axis('equal')

# Adjust the position of the chart
fig4.subplots_adjust(left=0.5)

# Configure the legend
legend_labels = [f'{label}: {percentual:.2f}%' for label, percentual in zip(r_metodos, percentuais_r_metodo)]
ax4.legend(wedges, legend_labels, loc='center left', bbox_to_anchor=(1.3, 0.5), title='Methods')

# Save the revenue chart per method
fig4.savefig('grafico_receitas_metodo.png', bbox_inches='tight')

# Move the graph files to the 'graphs' folder
files = os.listdir(path)
for file in files:
    if file.endswith('.png'):
        shutil.move(file, dest)