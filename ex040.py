n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2)/2
print(f"Um aluno que tirou {n1} e {n2} fica com a média {media:.2f}")
if media < 5:
    print("Você está \033[31mREPROVADO!\033[m")
elif media >= 5 and media < 7:
    print("Você está em \033[33mRECUPERAÇÃO!\033[m")
else:
    print("Você está \033[32mAPROVADO!\033[m")
