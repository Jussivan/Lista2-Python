numeros = []
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
novos_numeros = []
for numero in numeros:
    novos_numeros.append(numero * 2)
print("Lista original:", numeros)
print("Nova lista:", novos_numeros)