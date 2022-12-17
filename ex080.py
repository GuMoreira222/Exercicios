valores = list()
for i in range(0,5):
    num = int(input("Digite um valor: "))
    if i == 0 or num > valores[-1]:
        valores.append(num)
        print("O valor foi adicionado na posição final")
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f"O valor foi inserido na posição {pos}")
                break
            pos += 1
print("-="*30)   
print(f"Os valores digitados foram {valores}")