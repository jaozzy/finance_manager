texts = []

# Prompt the user to input the purchases one by one
print ('Digite as compras, uma a uma, seguindo a seguinte formatação:\n"{data(dd/mm/aaaa)}, {tipo-("d"=despesa/"r"=receita))}, {categoria-(saúde)}, {metodo-(débito)}, {valor-(xx.yy),}"\nNão esqueça da vígula no final de cada linha!\n"/off" Para gerar o arquivo .txt')

while True:
    # Get user input
    text = str(input('Digite aqui:    '))

    # Accumulate the entered data    
    data = ''.join(texts)

    if text == '/off':
        break
    
    # Write the accumulated data to the 'infos.txt' file
    texts.append(text + '\n')
    
# Write the accumulated data to the 'infos.txt' file
with open('infos.txt', 'w', encoding='utf8') as file:
    file.write(f'{data}\n')