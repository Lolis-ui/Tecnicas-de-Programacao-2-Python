#calcular área da circuferência

from math import pi

raio = float(input("Digite o valor do raio da circuferência: "))
area = (pi * raio**2)

print(f"O valor da aréa da circuferência de raio {raio} é igual a: {area:.2f}")