nome = 'Raphael'
nome_tamanho = len(nome)
i = 0
balde = ''
while i < nome_tamanho:
    balde += f'*{nome[i]}'
    i+= 1

print(balde)
