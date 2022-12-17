print("="*30)
print(f"{' '*5}LOJA PERSEVERANCE")
print("="*30)
soma = maior = c = menor = 0
nmb = ''
while True:
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    soma += preco
    c += 1
    if preco >= 1000:
        maior += 1
    if c == 1 or preco < menor:
        menor = preco
        nmb = nome
    resp = ' '
    while resp not in 'SN':
        resp = input("Deseja continuar? [S/N] ").strip().upper()[0]
    if resp == 'N':
        break
print(f"O total da compra foi R$ {soma:.2f}")
print(f"Temos {maior} produtos custando mais de R$ 1000,00")
print(f"O produto mais barato foi {nmb} e custou R$ {menor:.2f}")