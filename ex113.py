def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TabError):
            print('ERRO Por favor, digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interropida pelo usuário.\033[m')
            return 0
        else:
            return n

num = leiaInt('Digite um valor: ')
print(f'O valor digitado foi {num}')




