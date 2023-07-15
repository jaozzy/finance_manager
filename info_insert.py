texts = []

print ('Digite as compras, uma a uma, seguindo a seguinte formatação:\n"{data(dd/mm/aaaa)}, {local-("farmacia")}, {descricao-(remedio_x)}, {valor-(xx.yy)}"\n"/off" Para gerar o arquivo .txt')

while True:
    text = str(input('Digite aqui:    '))
    
    data = ''.join(texts)

    if text == '/off':
        break
    
    texts.append(text + '\n')
    
with open('infos.txt', 'w', encoding='utf8') as file:
    file.write(f'{data}\n')