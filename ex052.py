num = int(input("Digite um número: "))
v = 0
for i in range(1, num + 1):
    if num % i == 0:
        print("\033[33m", end=' ')
        v += 1
    else:
        print("\033[31m", end=' ')
    print(i, end=' ')
print(f"\n\033[mO número {num} foi divisível {v} vezes")
if v == 2:
    print("E por isso ele é PRIMO.")
else:
    print(("E por isso ele NÃO É PRIMO."))
