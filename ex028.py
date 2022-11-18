from random import randint
from time import sleep

computador = randint(0,5)
print ("-=-" * 20)
print ("Vou pensar em número entre 0 e 5. Tente adivinhar...")
print ("-=-" * 20 )
num = int(input("Em que número eu pensei? "))
print ("Processando...")
sleep(3)

if num == computador:
    print ("PARABÉNS! Você ganhou.")
else:
    print (f"Você perdeu! eu pensei no número {computador}.")