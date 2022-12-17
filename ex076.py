lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90,
        'Estojo', 25, 'Tranferidor', 4.20, 'Compasso', 9.99, 'Mochila',
        120.32, 'Canetas', 22.30, 'Livro', 34.90)
print("-"*40)
print(f'{"Listagem de preços":^40}')
print("-"*40)
for p in range(0, len(lista)):
    if p % 2 == 0:
        print(f"{lista[p]:.<30}", end=' ')
    else:
        print(f"R$ {lista[p]:>6.2f}")
print("-"*40)
    

