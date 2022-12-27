from time import sleep

def contador(i, f, p):
    print("-="*30)
    if p == 0:
        p = 1
    if i < f:
        print(f"Contagem regressiva de {i} até {f} de {p} em {p}")
        for c in range(i, f+1, p): 
            print(c, end=' ')
            sleep(0.5)
    elif i > f:
        if p > 0:
            print(f"Contagem regressiva de {i} até {f} de {p} em {p}")
            for c in range(i, f-1, -p):
                print(c, end=' ')
                sleep(0.5)
        elif p < 0:
            print(f"Contagem regressiva de {i} até {f} de {-p} em {-p}")
            for c in range(i, f-1, p):
                print(c, end=' ')
                sleep(0.5)
    print("FIM!")

contador(1, 10, 1)
contador(10, 0, 2)
print("-="*30)
print("Agora é sua vez de personalizar a contagem!")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)