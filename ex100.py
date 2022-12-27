from random import randint
from time import sleep

def sorteia(lst):
    print(f"Sorteando {len(lst)} valores da lista: ", end='')
    for c in range(0,5):
        n = randint(1,10)
        lst.append(n)
        print(n, end=' ')
        sleep(0.5)
    print("PRONTO!")

def somapar(lst):
    s = 0
    for n in lst:
        if n %2 == 0:
            s += n
    print(f"Somando os valores pares de {lst}, temos {s}")

nums = []
sorteia(nums)
somapar(nums)
