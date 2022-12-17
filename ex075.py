nums = (int(input("Digite um número: ")),
        int(input("Digite outro número: ")),
        int(input("Digite mais um número: ")),
        int(input("Digite o último número: ")))
print(f"Você digitou os valores {nums}")
print(f"O número 9 apareceu {nums.count(9)} vezes")
if 3 in nums:
    print(f"O número 3 apareceu na posição {nums.index(3)+1}")
else:
    print("O número 3 não apareceu")
print("Os números pares digitados foram ", end='')
for n in nums:
    if n %2 == 0:
        print(n, end=' ')
