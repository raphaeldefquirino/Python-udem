while True:
    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')
    operador = input('Digite o operador que deseja utilizar (+, -, /, *)')

    numeros_validos = None
    operadores_permitidos = '+-/*'
    try: 
        num1_convertido = float(num1)
        num2_convertido = float(num2)   
        numeros_validos = True
    except:
        ...

    if numeros_validos is None:
        print('Digite apenas números. ')
        continue

    if operador not in operadores_permitidos: 
        print('Operador inválido. ')
        continue

    if operador == '+': 
        print(num1_convertido +  num2_convertido)
    elif operador == '-':
        print(num1_convertido -  num2_convertido)
    elif operador == '/':
        print(num1_convertido /  num2_convertido)
    elif operador == '*':
        print(num1_convertido *  num2_convertido)

    sair = input('Você deseja encerrar o programa ? [s]im ').lower().startswith('s')

    if sair: 
        break