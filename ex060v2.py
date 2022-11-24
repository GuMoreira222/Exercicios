from math import factorial

x = int(input("Digite um número para calcular seu fatorial: "))
print(f"{x}! = ", end='')
for i in range(x, 0, -1):
    print(f" {i} ", end='')
    print("x" if i > 1 else "=", end='')
print(f" {factorial(x)}")
