def area(l, c):
    a = l * c
    print(f"A área de um terreno {l}x{c} é de {a:.2f}m²")
    
larg = float(input("Largura (m): "))
comp = float(input("Comprimento (m): "))
area(larg, comp)