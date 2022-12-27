def voto(nasc):
    from datetime import date
    ano = date.today().year 
    idade = ano - nasc
    if 15 < idade < 18 or idade > 70:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif 17 < idade < 71:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos: NÃO VOTA'

n = int(input("Ano de nascimento: "))
print(voto(n))