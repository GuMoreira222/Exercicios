vel = float(input("Qual é a velocidade atual do carro? "))
if vel > 80:
    multa = (vel - 80) * 7
    print ("MULTADO! Você excedeu o limite de 80 km/h")
    print (f"A multa será de R${multa:.2f}")
    print ("Tenha um bom dia. Dirija com segurança!")
else:
    print ("Tenha um bom dia. Dirija com segurança!")