homens = maior = menor = 0
while True:
    print("="*30)
    print(f"{' '*5}CADASTRE UMA PESSOA")
    print("="*30)
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input("Sexo [M/F]: ").strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        menor += 1
    print("="*30)
    cont = ' '
    while cont not in 'SN':
        cont = input("Deseja continuar [S/N]: ").strip().upper()[0]
    if cont == 'N':
        break
print(f"\nTemos um total de {maior} pessoas maiores de idade.")
print(f"Ao todo temos {homens} homens cadastrados.")
print(f"Temos {menor} mulheres com menos de 20 anos.\n")
