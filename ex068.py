from random import randint

print("=-"*20)
print("Vamos jogar PAR ou ÍMPAR")
print("=-"*20)
v = 0
while True:
    comp = randint(0,10)
    num = int(input("Digite um número: "))
    jog = ' '
    while jog not in 'PIÍ':
        jog = input("PAR ou ÍMPAR? ").strip().upper()[0]
    total = comp + num
    print("-"*30)
    print(f"Jogador jogou {num} e o computador {comp}. Total de {comp+num} ", end='')
    print("deu PAR" if total %2 == 0 else "deu ÍMPAR")
    print("-"*30)
    if total %2 == 0 and jog == 'P' or total%2 == 1 and jog in 'IÌ':
        print("JOGADOR VENCEU!")
        v += 1
    else:
        print("COMPUTADOR VENCEU!")
        break
    print("Vamos jogar novamente...")
print("=-"*20)
print(f"GAME OVER. Você venceu {v} vezes.")

