altura1 = float(input("Digite a altura da primeira pessoa: "))
altura2 = float(input("Digite a altura da segunda pessoa: "))
altura3 = float(input("Digite a altura da terceira pessoa: "))

if altura1 >= altura2 and altura1 >= altura3:
    maior = altura1
elif altura2 >= altura1 and altura2 >= altura3:
    maior = altura2
else:
    maior = altura3

if altura1 <= altura2 and altura1 <= altura3:
    menor = altura1
elif altura2 <= altura1 and altura2 <= altura3:
    menor = altura2
else:
    menor = altura3

if (altura1 != maior and altura1 != menor) or (altura1 == maior and altura1 == menor):
    mediana = altura1
elif (altura2 != maior and altura2 != menor) or (altura2 == maior and altura2 == menor):
    mediana = altura2
else:
    mediana = altura3

print(f"Maior altura: {maior}")
print(f"Altura mediana: {mediana}")
print(f"Menor altura: {menor}")