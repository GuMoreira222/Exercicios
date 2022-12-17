s = cont = 0
while True:
    num = int(input("Digite um número (999 para parar): "))
    if num == 999:
        break
    s += num
    cont += 1
print(f"Foram digitados {cont} números e a soma entre eles é {s}")