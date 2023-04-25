lista = []
for i in range(10):
    numero = int(input("Digite um número: "))
    lista.append(numero)
elementos_par = []
for i in range(len(lista)):
    if i % 2 == 0:
        elementos_par.append(lista[i])
print("Elementos de índice par:", elementos_par)
