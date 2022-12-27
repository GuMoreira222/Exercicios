def leiaint(msg):
    while True: 
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO! Digite um número inteiro válido.")
            continue
        except (KeyboardInterrupt):
            print("Usuário preferiu parar o programa.")
            return 0
        else:   
            return num
    
def leiafloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print("ERRO! Digite um número real válido.")
            continue
        except(KeyboardInterrupt):
            print("Usuário preferiu parar o programa.")
        else:
            return num

ni = leiaint("Digite um número inteiro: ")
nf = leiafloat("Digite um número real: ")
print(f"O número inteiro digitado foi {ni} e o real {nf}.")