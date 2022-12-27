from datetime import date

ano = date.today().year
cad = {}
cad['nome'] = input("Nome: ")
nasc = int(input("Ano de nascimento: "))
cad['idade'] = ano - nasc
cad['ctps'] = int(input("Carteira de trabalho (0 não tem): "))
if cad['ctps'] != 0:
    cad['contratação'] = int(input("Ano de contratação: "))
    cad['salário'] = float(input("Salário: R$ "))
    idcont = cad['contratação'] - nasc
    cad['aposentadoria'] = idcont + 35
print("="*50)
for k, v in cad.items():
    print(f"  - {k} tem o valor {v}.")