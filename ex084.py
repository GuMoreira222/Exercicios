pessoas = list()
dados = list()
maior = menor = 0
while True:
    dados.append(input("Nome: "))
    dados.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in 'SN':
        resp = input("Quer continuar? [S/N] ").strip().upper()[0]
    if resp == 'N':
        break
print(f"Ao todo você cadastrou {len(pessoas)} pessoas.")
print(f"O maior peso foi de {maior}kg. Peso de ", end='')
for p in pessoas:
    if p[1] == maior:
        print(f"[{p[0]}] ", end='')
print()
print(f"O menor peso foi de {menor}kg. Peso de ", end='')
for p in pessoas:
    if p[1] == menor:
        print(f"[{p[0]}] ", end='')


