print("-=-" * 20)
print("Analisador de triângulos")
print("-=-" * 20)

a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))
if a + b > c and a + c > b and b + c > a:
    print("Esses três segmentos formam um triângulo.")
else:
    print("Os segmentos não formam um triângulo.")
