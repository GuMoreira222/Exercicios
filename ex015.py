dias = int(input("Por quantos dias o carro foi alugado? "))
km = float(input("Quantos quilômetros rodados? "))
preco = (60 * dias) + (0.15 * km)
print (f"O valor a ser pago é de R${preco:.2f}")