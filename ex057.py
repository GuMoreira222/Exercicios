sexo = input("Digite o seu sexo [M/F]: ").strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    sexo = input("Dados inválidos... por favor, informe seu sexo: ").strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso.")