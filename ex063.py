print("-=-"*15)
print(f"{' '*9}Sequência de Fibonacci")
print("-=-"*15)
n = int(input("Quantos termos deseja? "))
cont = 2
penultimo = 0
ultimo = 1
print(penultimo, end=' -> ')
print(ultimo, end=' -> ')
while cont < n:
    termo = penultimo + ultimo
    print(termo, end='')
    print(" -> ", end='')
    penultimo = ultimo
    ultimo = termo
    cont += 1
print("FIM")
