from time import sleep

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
op = 0
while op != 5:
    print("[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa")
    op = int(input("Qual a sua opção? "))
    if op == 1:
        print(f"A soma entre os números {n1} e {n2} é {n1+n2}.")
    elif op == 2:
        print(f"A multiplicação entre os números {n1} e {n2} é {n1*n2}.")
    elif op == 3:
        if n1 > n2:
            print(f"Entre {n1} e {n2} o maior é {n1}.")
        elif n1 < n2:
            print(f"Entre {n1} e {n2} o maior é {n2}.")
        else:
            print(f"Os números {n1} e {n2} são iguais.")
    elif op == 4:
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif op == 5:
        print("Finalizando...")
        sleep(3)
    else:
        print("Opção inválida... Tente novamente.")
    print("-=-"*10)
print("Fim do programa. Volte sempre!")


