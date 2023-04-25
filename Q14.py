numeros = set()
for i in range(5):
    numeros.add(int(input("Digite um número: ")))
if 3 in numeros:
    print("O número 3 está presente no conjunto.")
else:
    print("O número 3 não está presente no conjunto.")