lista = list()
while True:
    lista.append(int(input("Digite um valor: ")))
    resp = ' '
    while resp not in 'SN':
        resp = input("Deseja continuar? [S/N] ").upper().strip()[0]
    if resp == 'N':
        break
print("-="*30)
lista.sort(reverse=True)
print(f"Foram digitados {len(lista)} elementos.")
print(f"A lista em ordem descrescente fica {lista}")
if 5 in lista:
    print("O valor 5 faz parte da lista")
else:
    print("O valor 5 não foi encontrado na lista")
