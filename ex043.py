peso = float(input("Digite o seu peso (kg): "))
alt = float(input("Digite sua altura (m): "))
imc = peso/(alt ** 2)
print(f"Seu imc é de {imc:.1f}")
print("Você está ", end='')
if imc < 18.5:
    print("ABAIXO DO PESO!")
elif 18.5 <= imc < 25:
    print("no PESO IDEAL!")
elif 25 <= imc < 30:
    print("com SOBRE PESO!")
elif 30 <= imc < 40:
    print("com OBESIDADE!")
else:
    print("com OBESIDADE MÓRBIDA!")