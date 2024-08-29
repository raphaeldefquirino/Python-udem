while True:
    palavra_usuario = input('Digite uma letra: ').lower()
    palavra_secreta = 'perfume'
    palavra_formatada = '*******'

    if len(palavra_usuario) > 1:
        print('Digite apenas uma letra. ')
        continue

    if palavra_usuario in palavra_secreta:
       
       if palavra_usuario == 'p':
           print('P de perfume')
    else: 
        print('Não está na palavra secreta. ')


