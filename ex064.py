cont = 0
num = 0
s = 0
num = int(input("Digite un número e [999 para parar]: "))
while num != 999:
    s += num
    cont += 1
    num = int(input("Digite un número e [999 para parar]: "))
print(f"Foram digitados {cont} números e a soma entre eles é {s}")