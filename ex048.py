a = 0
b = 0
for i in range(3,501,3):
    if i %2 == 1:
        a += i
        b += 1
print(f"A soma dos {b} valores ímpares e múltiplos de três é {a}")