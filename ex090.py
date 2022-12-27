aluno = {}
aluno['nome'] = input("Nome: ")
aluno['média'] = float(input(f"Média de {aluno['nome']}: "))
if aluno['média'] < 5:
    aluno['situação'] = 'reprovado'
elif aluno['média'] < 7:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'aprovado'
print("-="*25)
for k, v in aluno.items():
    print(f"{'-':>3} {k} é igual a {v}")