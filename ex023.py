from time import sleep

num = int(input("Digite um número de 0 a 9999: "))
while num < 0 or num > 9999:
    num = int(input("Digite um número de 0 a 9999: "))

else:

    print("Analisando o número...")
    sleep(2)

    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10

    print(f"Unidade: {u}")
    print(f"Dezena: {d}")
    print(f"Centena: {c}")
    print(f"Milhar: {m}")
