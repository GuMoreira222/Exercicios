valores = list()
while True:
    num = int(input("Digite um valor: "))
    if num in valores:
        print("Valor duplicado! Não vou adicionar... ")
    else:
        valores.append(num)
        print("Valor adicionado com sucesso... ")
    resp = ' '
    while resp not in 'SN':
        resp = input("Deseja continuar: [S/N] ").strip().upper()[0]
    if resp == 'N':
        break
print("-="*25)
valores.sort()
print(f"Você digitou os valores {valores}")