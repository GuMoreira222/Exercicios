s = 0
c = 0
for i in range(1,7):
    num = int(input("Digite um número: "))
    if num %2 == 0:
        s += num
        c += 1
print(f"Foram digitados {c} números pares e a soma entre eles é {s}")
