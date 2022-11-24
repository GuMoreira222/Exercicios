print("-=-"*10)
print(f"{' '*7}Gerador de PA")
print("-=-"*10)
primeiro = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))
cont = 0
while cont < 10:
    print(primeiro, end='')
    print(" -> ", end='')
    primeiro += r
    cont += 1
print("Acabou")