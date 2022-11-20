from datetime import date

atual = date.today().year
nascimento = int(input("Digite o ano de nascimento: "))
idade = atual - nascimento
if idade > 18:
    passado = idade - 18
    ano = atual - passado
    print(f"Quem nasceu em {nascimento} teve 18 anos em {ano}")
    print(f"Se passou {passado} anos do seu alistamento.")
elif idade < 18:
    falta = 18 - idade
    ano = atual + falta
    print(f"Quem nasceu em {nascimento} vai ter 18 anos em {ano}")
    print(f"Ainda lhe falta {falta} anos para se alistar.")
else:
    print(f"Quem nasceu em {nascimento} está com 18 anos em {atual}")
    print("É melhor correr e se alistar IMEDIATAMENTE.")