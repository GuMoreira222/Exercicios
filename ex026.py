frase = input("Digite uma frase: ").strip().upper()
print (f"A letra a aparece {frase.count('A')} vezes")
print (f"A primeira letra a aparece na posição {frase.find('A') + 1}")
print (f"A última letra a aparece na posição {frase.rfind('A') + 1}")