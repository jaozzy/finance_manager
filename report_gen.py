from docx import Document
from manager import extra_infos
from datetime import datetime
from essencials import get_path

def generate_report():
    
    agora = datetime.now()
    data_formatada = agora.strftime("%d/%m/%Y %H:%M")
    
    # Obtém as informações do relatório da função extra_infos
    gastos_total, data_min, data_max, periodo, periodo_str, gcat = extra_infos()

    # Cria um novo documento do Word
    doc = Document()

    # Adiciona o título do relatório
    doc.add_heading('Relatório Financeiro', level=1)
    doc.add_paragraph(f'Gráfico Gerado em {data_formatada} às {agora.strftime("%H:%M")}')

    # Adiciona as informações do relat  ório
    doc.add_paragraph(f'Total gasto no período analisado: {gastos_total:.2f}R$')
    doc.add_paragraph(f'Data mais antiga analisada: {data_min.strftime("%d/%m/%Y")}')
    doc.add_paragraph(f'Data mais recente analisada: {data_max.strftime("%d/%m/%Y")}')
    doc.add_paragraph(f'Período de Análise: {periodo_str}')

    # Adiciona os detalhes de gastos por categoria
    doc.add_heading('Detalhes de Gastos por Categoria', level=2)

    for categoria, gasto in gcat.items():
        mdia = (gasto / periodo.days)
        gperc = (gasto / gastos_total) * 100
        doc.add_paragraph(f'O total gasto em {categoria} no período analisado foi de {gasto:.2f}R$')
        doc.add_paragraph(f'A média de gasto diário foi de aproximadamente {mdia:.2f}R$, representando {gperc:.2f}% do valor total gasto no período analisado.')
        doc.add_paragraph()  # Adiciona uma quebra de linha entre os detalhes


    # Salva o documento em um arquivo .docx
    doc.save('relatorio.docx')

# Chama a função para gerar o relatório
generate_report()
