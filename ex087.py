matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = soma2 = 0
for l in range(0, 3):
    for c in range(0 ,3):
        matriz[l][c] = int(input(f"Digite um valor para a posição [{l}, {c}]: "))
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
        soma2 += matriz[l][2]
print("-="*25)
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end='')
    print()
print("-="*25)
print(f"A soma dos valores pares é {somap}.")
print(f"A soma dos valores da terceira coluna é {soma2}.")
print(f"O maior valor da segunda linha é {max(matriz[1])}")