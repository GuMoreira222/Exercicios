import moeda

valor = float(input("Digite o preço: R$"))
print(f"A metade de R$ {moeda.moeda(valor)} é R$ {moeda.moeda(moeda.metade(valor))}")
print(f"O dobro de R$ {moeda.moeda(valor)} é R$ {moeda.moeda(moeda.dobro(valor))}")
print(f"Aumentando 10%, temos R$ {moeda.moeda(moeda.aumentar(valor, 10))}")