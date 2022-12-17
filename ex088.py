from random import randint

print("-"*30)
print(f"{' '*5} Sorteio Mega Sena")
print("-"*30)
jogos = int(input("Digite quantos jogos quer que eu sorteie: "))
lista = []
sorteios = []
c = 0
while c < jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont == 6:
            break
    sorteios.append(lista[:])
    lista.clear()
    c += 1

for c1, j in enumerate(sorteios):
    print(f"O {c1+1}º jogo sorteado foi {j}")
    
    