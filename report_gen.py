from docx import Document
from manager import extra_infos
from datetime import datetime
from essencials import get_path, file_exists

path = get_path()
graphdir = f'{path}/graphs/'

file_exists('relatorio.docx')

def generate_report():
    
    agora = datetime.now()
    data_formatada = agora.strftime("%d/%m/%Y")
    
    # Obtém as informações do relatório da função extra_infos
    receitas, receitas_total, receitas_met, receitas_cat, despesas, despesas_total, despesas_met, despesas_cat, supv, percD_R, percD_M, percD_C, percR_M, percR_C, data_min, data_max, periodo, periodo_str, mdia_d_D, mdia_r_D = extra_infos()
    
    # Cria um novo documento do Word
    doc = Document()

    # Adiciona o título do relatório
    doc.add_heading('Relatório Financeiro', level=1)
    doc.add_paragraph(f'Relatório Gerado em {data_formatada} às {agora.strftime("%H:%M")}')
    doc.add_paragraph('Desenvolvido por: João Pedro')
    doc.add_paragraph('Contato: (47) 9 99783190 / servicecontact.joao@gmail.com')
    doc.add_paragraph('')

    # Adiciona as informações do relatório
    doc.add_heading('Informações Gerais:')
    doc.add_paragraph(f'Total gasto no período analisado: R${despesas_total}')
    doc.add_paragraph(f'Total recebido no período analisado: R${receitas_total}')
    doc.add_paragraph(f'Superávit/Défict: R${supv}')
    doc.add_paragraph(f'Data mais antiga analisada: {data_min.strftime("%d/%m/%Y")}')
    doc.add_paragraph(f'Data mais recente analisada: {data_max.strftime("%d/%m/%Y")}')
    doc.add_paragraph(f'Período de Análise: {periodo_str}')

    # Adiciona os detalhes de gastos por categoria
    doc.add_heading('Detalhes de Gastos por Categoria', level=2)

    for despesa, categoria in despesas_cat.items():
        despesa, categoria = categoria, despesa
        despesa = float(despesa)  # Converte despesa para tipo numérico
        mdia = despesa / periodo.days if periodo.days != 0 else 0
        gperc = (despesa / despesas_total) * 100
        doc.add_paragraph(f'O total gasto em {categoria} no período analisado foi de {despesa}R$')
        doc.add_paragraph(f'A média de gasto diário com {categoria} foi de aproximadamente {mdia:.2f}R$, representando {gperc:.2f}% do valor total de gastos do período analisado.')
    doc.add_paragraph() # Adiciona uma quebra de linha entre os detalhes
        
    doc.add_heading('Gráfico de Setores Relacionado às Despesas por Categoria em Função das Despesas totais do Periodo Analisado:', level=2)
    doc.add_picture(f'{graphdir}/grafico_despesas_categoria.png')
    
    doc.add_page_break()
    
    # Adiciona os detalhes de gastos por categoria
    doc.add_heading('Detalhes de Gastos por Método de Pagamento', level=2)

    for despesa, metodo in despesas_met.items():
        despesa, metodo = metodo, despesa
        mdia = (despesa / periodo.days)
        gperc = (despesa / despesas_total) * 100
        doc.add_paragraph(f'O total gasto por {metodo} no período analisado foi de {despesa}R$')
        doc.add_paragraph(f'A média de gasto diário por {metodo} foi de aproximadamente {mdia:.2f}R$, representando {gperc:.2f}% do valor total de gastos do período analisado.')
        doc.add_paragraph() # Adiciona uma quebra de linha entre os detalhes
        
    doc.add_heading('Gráfico de Setores Relacionado às Despesas por Método de Pagamento em Função das Despesas totais do Periodo Analisado:', level=2)
    doc.add_picture(f'{graphdir}/grafico_despesas_metodo.png')
    
    doc.add_page_break()

    doc.add_heading('Detalhes de Receitas por Categoria:', level=2)

    for receita, categoria in receitas_cat.items():
        receita, categoria = categoria, receita
        mdia = (receita / periodo.days)
        rperc = (receita / receitas_total) * 100
        doc.add_paragraph(f'O total recebido em {categoria} no período analisado foi de R${receita}')
        doc.add_paragraph(f'A média de recebimento diário foi de aproximadamente R${mdia:.2f}, representando {rperc:.2f}% do valor total de gastos do período analisado.')
        doc.add_paragraph() # Adiciona uma quebra de linha entre os detalhes
        
    doc.add_heading('Gráfico de Setores Relacionado às Receitas por Categoria em Função das Receitas totais do Periodo Analisado:', level=2)
    doc.add_picture(f'{graphdir}/grafico_receitas_categoria.png')
    
    doc.add_page_break()
    
    doc.add_heading('Detalhes de Receitas por Método de Pagamento:', level=2)

    for receita, metodo in receitas_met.items():
        receita, metodo = metodo, receita
        mdia = (receita / periodo.days)
        rperc = (receita / receitas_total) * 100
        doc.add_paragraph(f'O total recebido por {metodo} no período analisado foi de R${receita}')
        doc.add_paragraph(f'A média de recebimento diário foi de aproximadamente R${mdia:.2f}, representando {rperc:.2f}% do valor total de gastos do período analisado.')
        doc.add_paragraph() # Adiciona uma quebra de linha entre os detalhes
        
    doc.add_heading('Gráfico de Setores Relacionado às Receitas por Método de Pagamento em Função das Receitas totais do Periodo Analisado:', level=2)
    doc.add_picture(f'{graphdir}/grafico_receitas_metodo.png')
    
    # Salva o documento em um arquivo .docx
    doc.save('relatorio.docx')

# Chama a função para gerar o relatório'''
generate_report()
