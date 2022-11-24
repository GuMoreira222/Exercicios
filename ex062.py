print("-=-"*10)
print(f"{' '*7}Gerador de PA")
print("-=-"*10)
primeiro = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))
termos = primeiro
cont = 1
while cont <= 10:
    print(termos, end='')
    print(" -> ", end='')
    termos += r
    cont += 1
print("Pausa")
x = 1
i = 0
cont1 = 0
while x != 0:
    x = int(input("Quantos termos você quer mostrar a mais? "))
    i = x + cont1
    while cont1 < i:
        print(termos, end='')
        print(" -> ", end='')
        termos += r
        cont1 += 1
    if x != 0: 
        print("Pausa")  
print(f"Progressão finalizada com {(cont + cont1) - 1} termos mostrados.")
     
    