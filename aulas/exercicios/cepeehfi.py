cpf = '578.306.768-79'
cpf = cpf.replace('-', '')
cpf = cpf.replace('.', '')

resultado = 0
contador = 10

for i in range(0, 9):
    resultado += int(cpf[i]) * contador
    contador -= 1

resultado = (resultado * 10) % 11

if resultado > 9:
   resultado = 0
else: 
    resultado = resultado

if str(resultado) == cpf[9]:
    resultado = 0
    contador = 11

    for i in range(0, 10):
        resultado += int(cpf[i]) * contador
        contador -= 1

    resultado = (resultado * 10) % 11

    if resultado > 9:
        resultado = 0
    else: 
        resultado = resultado

    if str(resultado) == cpf[10]:
        print(f'{cpf} válido')
    else: 
        print(False)
else:
    print(False)
