from time import sleep
from random import randint

computador = randint(0,2)
print("Suas opções: \n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA")
jogador = int(input("Qual a sua jogada? "))
while jogador < 0 or jogador > 2:
    print("Jogada Inválida... Tente novamente.")
    print("Suas opções: \n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA")
    jogador = int(input("Qual a sua jogada? "))
else:
    itens = ('Pedra', 'Papel', 'Tesoura')
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!")
    print("-=-"*10)
    print(f"Computador jogou {itens[computador]}\nJogador jogou {itens[jogador]}")
    print("-=-"*10)
    if computador == 0:
        if jogador == 0:
            print("EMPATE!")
        elif jogador == 1:
            print("JOGADOR VENCEU!")
        elif jogador == 2:
            print("COMPUTADOR VENCEU!")
    elif computador == 1:
        if jogador == 0:
            print("COMPUTADOR VENCEU!")
        elif jogador == 1:
            print("EMPATE!")
        elif jogador == 2:
            print("JOGADOR VENCEU!")
    elif computador == 2:
        if jogador == 0:
            print("JOGADOR VENCEU!")
        elif jogador == 1:
            print("COMPUTADOR VENCEU!")
        elif jogador == 2:
            print("EMPATE!")
        


