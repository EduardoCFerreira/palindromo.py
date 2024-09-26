while True:
    palavra = input('Digite uma palavra: ').lower()

    palavra_valida = None

    try:
        palavra_str = str(palavra)
        palavra_valida = True
    except:
        palavra_valida = False

    if palavra_valida is None:
        print('Você não digitou nada')
        continue

    tamanho_palavra = len(palavra) + 1
    palavra_mudada = palavra[-1:-tamanho_palavra:-1]

    if palavra == palavra_mudada:
        print(f'Sua palavra mudada é {palavra}')
        print('Sua palavra é um palindromo')
    else:
        print('Sua palavra não é um palindromo')
    
    sair = input('Deseja sair? [S]im: ').lower().startswith('s')
    if sair:
        print('Saiu')
        break