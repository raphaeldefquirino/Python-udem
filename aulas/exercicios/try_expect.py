numero_str = input('Digite um númeo para ser dobrado: ')

try: 
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2}')
except: 
    print('Você não digitou um número. ')