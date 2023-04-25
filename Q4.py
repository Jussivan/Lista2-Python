numeros = set(input("Digite 5 números separados por espaço: ").split())
print("Números: ", numeros)
remover = input("Escolha um número para remoção: ")
if remover in numeros:
    numeros.remove(remover)
    print("O número", remover, "foi removido do conjunto.")
print("O conjunto atualizado é: ", numeros)