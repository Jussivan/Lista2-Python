nomes = tuple(input(f"Digite o {i+1}º nome: ") for i in range(3))
print(f"Os nomes digitados foram: {nomes}")
alterar = input("Escolha um nome para substituir: ")
novo_nome = input("Digite o novo nome: ")
if alterar in nomes:
    novos_nomes = tuple(novo_nome if nome == alterar else nome for nome in nomes)
    print(f"Os novos nomes digitados são: {novos_nomes}")
