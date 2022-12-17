valores = []
maior = menor = 0
for v in range(0, 5):
    valores.append(int(input(f"Digite o valor na posição {v}: ")))
    if v == 0:
        maior = menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
print("-="*30)
print(f"Os valores digitados foram {valores}")
print(f"O maior valor foi {maior} e foi digitado na posição ", end='')
for i, c in enumerate(valores):
    if c == maior:
        print(f"{i}...", end=' ')
print()
print(f"O menor valor foi {menor} e foi digitado na posição ", end='')
for i, c in enumerate(valores):
    if c == menor:
        print(f"{i}...", end=' ')
print()