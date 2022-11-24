from random import randint

comp = randint(0,10)
print("Sou seu computador...")
print("Acabei de pensar em número entre 0 e 10.")
print("Será que você consegue advinhar qual foi?")
jogador = int(input("Qual seu palpite? "))
while jogador > 10 or jogador < 0:
    jogador = int(input("Digite um número entre 0 e 10. Qual seu palpite? "))
tent = 1
while jogador != comp:
    tent += 1
    if jogador < comp:
        print("Mais... Tente novamente.")
        jogador = int(input("Qual seu palpite? "))
    else:
        print("Menos... Tente novamente.")
        jogador = int(input("Qual seu palpite? "))
print(f"Acertou na {tent}ª tentativa, PARABÉNS.")
