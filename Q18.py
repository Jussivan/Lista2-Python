dicionario = {}
for i in range(3):
    chave = input("Digite a chave do dicionário: ")
    valor = input("Digite o valor da chave: ")
    dicionario[chave] = valor
cidade = input("Digite a cidade em que você nasceu: ")
dicionario['cidade'] = cidade
print(dicionario)