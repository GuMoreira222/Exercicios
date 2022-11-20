num = int(input("Digite um número inteiro: "))
print("[ 1 ] BINÁRIO\n[ 2 ] OCTAL\n[ 3 ] HEXADECIMAL")
opcao = int(input("Escolha uma base de conversão: "))

if opcao == 1:
    print(f"{num} em BINÁRIO é {bin(num)[2:]}.")
elif opcao == 2:
    print(f"{num} em OCTAL é {oct(num)[2:]}.")
elif opcao == 3:
    print(f"{num} em HEXADECIMAL é {hex(num)[2:]}")
else:
    print("\033[31mERRO...\033[m Tente novamente!")
