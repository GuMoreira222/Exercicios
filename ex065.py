s = cont = maior = menor = 0
continuar = 's'
while continuar in 'S':
    num = int(input("Digite um número: "))
    continuar = input("Deseja continuar [S/N]: ").upper().strip()[0]
    s += num
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = s/cont
print(f"Você digitou {cont} números e a média foi {media:.2f}")
print(f"O maior valor foi {maior} e o menor foi {menor}")
