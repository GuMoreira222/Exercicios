nums = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
        'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
        'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
        'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
        'Dezenove', 'Vinte')
while True:
    x = int(input("Digite um número entre 0 e 20: "))
    while 0 < x > 20:
        x = int(input("Tente novamente. Digite um número entre 0 e 20: "))
    print(f"Você digitou o número {nums[x]}")
    resp = ' '
    while resp not in 'SN':
        resp = input("Deseja continuar? [S/N] ").strip().upper()[0]
    if resp in 'N':
        break