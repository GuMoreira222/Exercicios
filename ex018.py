from math import sin, cos, tan, radians

a = float(input("Digite o ângulo: "))
x = radians(a)
s = sin(x)
c = cos(x)
t = tan(x)

print (f"O ângulo de {a} tem o seno de {s:.2f}")
print (f"O ãngulo de {a} tem o cosseno de {c:.2f}")
print (f"O ãngulo de {a} tem a tangente de {t:.2f}")

