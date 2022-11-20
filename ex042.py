print("\033[33m-=-\033[m" * 20)
print("Analisador de triângulos")
print("\033[33m-=-\033[m" * 20)

a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Os segmentos formam um triângulo EQUILÁTERO.")
    elif a != b != c != a:
        print("Os segmentos formam um triângulo ESCALENO.")
    else:
        print("Os segmentos formam um triângulo ISÓCELES.")
else:
    print("Os segmentos não formam um triângulo.")