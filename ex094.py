grupo = []
pessoa = {}
somaid = 0
while True:
    pessoa['nome'] = input("Nome: ")
    pessoa['sexo'] = input("Sexo: [M/F] ")
    while pessoa['sexo'] not in 'MmFf':
        print("ERRO! Por favor, digite apenas M ou F.")
        pessoa['sexo'] = input("Sexo: [M/F] ")
    pessoa['idade'] = int(input("Idade: "))
    somaid += pessoa['idade']
    grupo.append(dict(pessoa))
    resp = input("Dejesa continuar? [S/N] ")
    while resp not in 'SsNn':
        print("ERRO! Responda apenas S ou N.")
        resp = input("Dejesa continuar? [S/N] ")
    if resp in 'Nn':
        break
media = somaid/len(grupo)
print("-="*30)
print(f"A) Ao todo temos {len(grupo)} pessoas cadastradas.")
print(f"B) A média de idade entre essas pessoas é {media:.2f}")
print("C) As mulheres cadastradas foram ", end='')
for p in grupo:
    if p['sexo'] in 'Ff':
        print(p['nome'], end=' ')
print()
print("D) Lista de pessoas que estão acima da média: ")
for p in grupo:
    if p['idade'] > media:
        print("   ", end='')
        for k, v in p.items():
            print(f"{k} = {v};", end=' ')
        print()
print("<< ENCERRADO >>")

