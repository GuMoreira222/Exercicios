def leiadinheiro(txt):
    from ex111.utilidadesCev import moeda
    v = False
    while not v:
        entrada = input(txt).replace(",",".").strip()
        if entrada.isalpha() or entrada == '':
            print(f"ERRO! '{entrada}' é um preço inválido.")
        else:
            v = True
            return float(entrada)