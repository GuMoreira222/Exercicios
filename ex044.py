from time import sleep

print("\033[31m=\033[m" * 60)
print("\033[31m-=-\033[m" * 20)
print("LOJA PERSEVERANCE")
print("\033[31m-=-\033[m" * 20)
print("\033[31m=\033[m" * 60)

valor = float(input("Qual o preço das compras? R$"))
print("[ 1 ] À vista dinheiro/cheque\n[ 2 ] À vista no cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão")
opcao = int(input("Escolha a opção de pagamento: "))
print("PROCESSANDO...")
sleep(2)
if opcao == 1:
    preco = valor - (valor*10/100)
    print(f"Sua compra de R${valor:.2f} ficará no final por R${preco:.2f}")
elif opcao == 2:
    preco = valor - (valor*5/100)
    print(f"Sua compra de R${valor:.2f} ficrá no final por R${preco:.2f}")
elif opcao == 3:
    parcela = valor/2
    print(f"Sua compra de R${valor:.2f} fica em 2x de R${parcela:.2f} sem juros.")
    print(f"Sua compra de R${valor:.2f} vai custar no final R${valor:.2f}")
elif opcao == 4:
    vezes = int(input("Em quantas vezes deseja? "))
    parcela = (valor + (valor*20/100))/vezes
    print(f"Sua compra será parcelada em {vezes} vezes de R${parcela:.2f} com juros.")
    print(f"Sua compra de R${valor:.2f} vai custar no final R${valor + (valor*20/100):.2f}")
else:
    print("Erro... Tente novamente!")
    
