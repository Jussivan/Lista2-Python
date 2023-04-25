numeros = set()
for i in range(10):
    numero = int(input("Digite um número: "))
    numeros.add(numero)
numeros = set(filter(lambda x: x % 2 != 0, numeros))
print("O conjunto com somente números ímpares é:", numeros)
