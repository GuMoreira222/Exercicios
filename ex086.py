matriz = [[], [], []]
c1 = c2 = c3 = 0
for c in range(0, 9):
    num = int(input(f"Digite um valor para [{c1}, {c2}]: "))
    c2 += 1
    if c2 == 3:
        c2 = 0
        c1 += 1
    if c <= 2:
        matriz[0].append(num)
    elif c <= 5:
        matriz[1].append(num)
    else:
        matriz[2].append(num)
print("-="*25)
for l in matriz:
    for n in l:
        print(f"[ {n} ]", end='')
        c3 += 1
        if c3 == 3:
            print()
            c3 = 0
