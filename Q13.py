dicionario = {}
while True:
    chave = input("Digite uma chave (ou digite 'sair' para encerrar): ")
    if chave == 'sair':
        break
    valor = input("Digite um valor para a chave '{}': ".format(chave))
    dicionario[chave] = valor
if 'profissão' in dicionario.keys():
    print("A chave 'profissão' está presente no dicionário!")
else:
    print("A chave 'profissão' não está presente no dicionário.")