maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input(f"Digite o peso da {i}ª pessoa: "))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O maior peso lido foi {maior:.1f}kg\nO menor peso lido foi {menor:.1f}kg")
        

