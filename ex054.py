from datetime import date

atual = date.today().year
maior = 0
menor = 0
for i in range(1, 8):
    ano = int(input(f"Digite em que ano nasce a {i}º pessoa: "))
    if atual - ano >= 21:
        maior += 1
    else:
        menor += 1
if maior > 0 and menor > 0:
    print(f"\nTivemos ao todo {maior} pessoas maiores de idade\nE tivemos {menor} pessoas menores de idade")
elif maior == 0:
    print("\nNão tivemos pessoas maiores de idade, apenas menores.")
else:
    print("\nNão tivemos pessoas menores de idade, apenas maiores.")
    