from math import factorial

x = int(input("Digite um número para calcular seu fatorial: "))
i = x
print(f"{x}! = ", end='')
while i > 0:
    print(f" {i} ", end='')
    print("x" if i > 1 else "=", end='')
    i -= 1
print(f" {factorial(x)}")



