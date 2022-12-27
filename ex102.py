def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: O valor do fatorial de um número num.
    """
    fat = 1
    print("="*30)
    for c in range(num, 0, -1):
        fat *= c
        if show == True:
            print(f"{c}", end='')
            print(" x " if c > 1 else " = ", end='')
    return fat
    
print(fatorial(5, True))

