lista = list()
pares = list()
impares = list()
while True:
    num = int(input("Digite um valor: "))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    r = ' '
    while r not in 'SN':
        r = input("Deseja continuar? [S/N] ").strip().upper()[0]
    if r == 'N':
        break
print("-="*30)
print(f"A lista completa é {lista}")
print(f"A lista dos números pares é {pares}")
print(f"A lista dos números ímpares é {impares}")