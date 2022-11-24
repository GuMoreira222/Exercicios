frase = input("Digite uma frase: ").upper().strip()
p = frase.split()
j = ''.join(p)
inv = j[::-1]
print(f"A frase {frase} ivertida fica {inv}")
if inv == j:
    print("Essa frase é um PALÍNDROMO.")
else:
    print("Essa frase não é um PALÍNDROMO.")