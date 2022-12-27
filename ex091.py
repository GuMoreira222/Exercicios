from time import sleep
from random import randint
from operator import itemgetter

dado = {'jogador 1': randint(1,6),
        'jogador 2': randint(1,6),
        'jogador 3': randint(1,6),
        'jogador 4': randint(1,6)}
ranking = {}
print("Valores sorteados: ")
for k, v in dado.items():
    print(f"{k} tirou {v} no dado.")
    sleep(1)
print("="*30)
print("  == RANKING DOS JOGADORES ==")
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
for c, v in enumerate(ranking):
    print(f"   {c+1}º lugar: {v[0]} com {v[1]}")
    sleep(1)
    

