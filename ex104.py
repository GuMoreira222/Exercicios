def leiaInt(msg):
    while True:   
        num = input(msg)
        if num.isnumeric():
            num = int(num)
            break
        elif '-' in num:
            if num.replace("-","").isnumeric():
                num = int(num)
                break
            else:
                print("\033[31mERRO! Digite um número inteiro válido.\033[m")
        else:
            print("\033[31mERRO! Digite um número inteiro válido.\033[m")
    return num

n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}.")
