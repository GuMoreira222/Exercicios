from datetime import date

nasc = int(input("Ano de nascimento do atleta: "))
idade = date.today().year - nasc
print(f"O atleta tem {idade} anos de idade.")
if idade <= 9:
    print("Sua categoria é MIRIM.")
elif idade <= 14:
    print("Sua categoria é INFANTIL.")
elif idade <= 19: 
    print("Sua categoria é JÚNIOR.")
elif idade <= 25:
    print("Sua categoria é SÊNIOR.")
else:
    print("Sua categoria é MASTER.")