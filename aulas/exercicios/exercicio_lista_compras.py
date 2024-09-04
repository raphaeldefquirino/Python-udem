import os

lista = [] #Cria o array da lista que servira para guardar os produtos.

while True: #Loop infinito para sempre rodar as opções
    opcao = input('''Selecione uma opção: 
[i]nserir [a]pagar [l]istar: ''').lower() #Variável para armazenar a opção que o usuário digitar.

    if len(opcao) > 1: #Condição para verificar se o usuário digitou mais de um caracter.
        print('Opção inválida')
        continue
    
    if opcao == 'i': 
        os.system('cls')
        produto = input('Digite o nome do produto que deseja inserir: ')
        lista.append(produto) #Método para inseririr no array o produto digitado (vai sempre colocar ao final da lista).
    elif opcao == 'a': 
        os.system('cls')
        if not lista:#Condição para verificar se a lista está vazia. 
            print('Não há produtos na lista para serem apagados')
        else: 
            indice = input('Qual o indicie do produto que deseja apagar ? ')
            try:
                del lista[int(indice)] #Método para apagar um item da lista.
            except ValueError: 
                print('Digite apenas números interios') 
            except IndexError:
                print("Índicie do produto não encontrado")
    elif opcao == 'l':
        os.system('cls')
        if not lista: 
            print('Não há produtos para serem litados')
        else:
            for item in enumerate(lista): #Método que vai retornar a lista enumerada 
                print(item)
    else: 
        print('Opção invalida. ')
    
    