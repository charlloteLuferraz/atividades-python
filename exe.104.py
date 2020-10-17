def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO!Digite inteiro válido.\033[n')
            if ok:
                break
        return valor
n = leiaInt('Digite um valor: ')
print(f'Voçẽ acabou de digitar o número {n}')

