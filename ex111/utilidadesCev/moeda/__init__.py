def aumentar(num, taxa, format=False):
    num = num + (num*(taxa/100))
    if format == True:
        return moeda(num)
    else:
        return num

def diminuir(num, taxa, format=False):
    num = num - (num*(taxa/100))
    if format == True:
        return moeda(num)
    else:
        return num

def dobro(num, format=False):
    num *= 2
    if format == True:
        return moeda(num)
    else:
        return num

def metade(num, format=False):
    num /= 2
    if format == True:
        return moeda(num)
    else:
        return num

def moeda(preco=0, moeda='R$'):
    return f"{moeda}{preco:>.2f}".replace(".",",")

def resumo(num, ta, td):
    print("-"*30)
    print(f"{'RESUMO DO VALOR':^30}")
    print("-"*30)
    print(f"{'Preço analisado:':20} {moeda(num)}")
    print(f"{'Dobro do preço:':20} {dobro(num, True)}")
    print(f"{'Metade do preço:':20} {metade(num, True)}")
    print(f"{f'{ta}% de aumento:':20} {aumentar(num, ta, True)}")
    print(f"{f'{td}% de dimuição:':20} {diminuir(num, td, True)}")
    print("-"*30)

