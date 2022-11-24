si = 0
mih = 0
nv = 0 
tm = 0
for i in range(1,5):
    print(f"{'-'*4}{i}ª Pessoa{'-'*4}")
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip()
    si += idade
    if i == 1 and sexo in 'Mm':
        mih = idade
        nv = nome
    if sexo in 'Mm' and idade > mih:
        mih = idade
        nv = nome
    if sexo in 'Ff' and idade < 20:
        tm += 1
media = si/4
print(f"\nA média de idade das pessoas é {media:.1f}")
print(f"O homem mais velho tem {mih} anos e se chama {nv}")
print(f"Dessas pessoa {tm} mulheres tem menos de 20 anos")