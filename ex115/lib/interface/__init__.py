def linha():
    print("="*45)

def cab(msg):
    linha()
    print(f"{msg:^45}")
    linha()

def leiaint(msg):
    while True: 
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mUsuário preferiu parar o programa.\033[m")
            return 0
        else:   
            return num

def menu(lista):
    c = 1
    cab("MENU PRINCIPAL")
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[m")
        c += 1
    linha()
    resp = leiaint("\033[32mSua opção: \033[m")
    return resp

