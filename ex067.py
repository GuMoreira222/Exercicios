while True:
    num = int(input("Digite um número para ver sua tabuada: "))
    if num < 0:
        break
    for i in range(1,11):
        print(f"{num} x {i:2} = {num*i}")