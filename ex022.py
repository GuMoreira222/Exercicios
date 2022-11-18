from time import sleep

nome = input("Digite seu nome completo: ").strip()
print ("Analisando seu nome...\n")
sleep(3)

print (f"O nome em letras maíusculas fica {nome.upper()}")
print (f"O nome em letras minúsculas fica {nome.lower()}")
letras = len(nome.replace(" ",""))
print (f"O nome tem {letras} letras")
nome1 = nome.split()
letras1 = len(nome1[0])
print (f"Seu primeiro nome é {nome1[0]} e tem {letras1} letras")