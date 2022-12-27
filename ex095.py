time = []
gols = []
jogador = {}
while True:
    jogador['nome'] = input("Nome do jogador: ")
    pt = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    for c in range(0, pt):
        gols.append(int(input(f"Quantos gols na partida {c+1}? ")))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    gols.clear()
    time.append(dict(jogador))
    resp = ' '
    while resp not in 'SN':
        resp = input("Quer continuar? [S/N] ").strip().upper()[0]
    if resp == 'N':
        break
print("-="*30)
print("cod ", end='')
for k in jogador.keys():
    print(f"{k:<15}", end='')
print()
print("-"*45)
for c, p in enumerate(time):
    print(f"{c:>3}", end=' ')
    for v in p.values():
        print(f"{str(v):<15}", end='')
    print()
while True:
    print("-"*45)
    dados = int(input("Mostrar dados de qual jogador? (999 interrompe) "))
    if dados == 999:
        break
    if dados >= len(time):
        print(f"ERRO! Não existe jogador com código {dados}.")
    else:  
        print(f" -- LEVANTAMENTO DO JOGADOR {time[dados]['nome']}:")
        for c, p in enumerate(time[dados]['gols']):
            print(f"   No jogo {c+1} fez {p} gols")
print(" << VOLTE SEMPRE >>")
    

