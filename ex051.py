print("="*30)
print(f"{' '*5}10 termos de uma PA")
print("="*30)
pt = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
d = pt + (10 - 1) * r
for i in range(pt,d+r,r):
    print(i, end='')
    print(" -> ", end='')
print("Acabou")
