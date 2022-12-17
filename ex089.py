from time import sleep
alunos = []
dados = []
while True:
    dados.append(input("Nome: "))
    dados.append(float(input("Nota 1: ")))
    dados.append(float(input("Nota 2: ")))
    alunos.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in 'SN':
        resp = input("Deseja continuar? [S/N] ").strip().upper()[0]
    if resp == 'N':
        break
print("-="*20)
print(f"{'Nº':<} {'Nome':<15} {'Média':>}")
print("-"*30)
for c, a in enumerate(alunos):
    media = (a[1] + a[2])/2
    print(f"{c:<2} {a[0]:<15} {media:>.1f}")
while True:
    print("-"*30)
    r = int(input("Notas de qual aluno? (999 interrompe) "))
    if r == 999:
        break
    print(f"Notas de {alunos[r][0]} são {alunos[r][1:3]}")
print("-"*30)
print("FINALIZANDO...")
sleep(2)
print("<<< Volte sempre >>>")