valor = int(input("Quanto deseja sacar? "))
quant = 0
nota = 50
while True:
    if valor >= nota:
        valor -= nota
        quant += 1
    else:
        if quant > 0:
            print(f"Foram usadas {quant} cédulas de R${nota:.2f}")
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        quant = 0
        if valor == 0:
            break