
palavra_secreta = 'perfume'

letras_acertadas = ''

while True:

    palavra_usuario = input('Digite uma letra: ').lower()
    if len(palavra_usuario) > 1:
        print('Digite apenas uma letra. ')
        continue

    if palavra_usuario in palavra_secreta:
       letras_acertadas += palavra_usuario
    palavra_formatada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formatada += letra_secreta
            
        else: 
            palavra_formatada += '*'
        
    print(palavra_formatada)

    if palavra_formatada == palavra_secreta:
        print('VOCÊ GANHOU!!')
        break

  
    

