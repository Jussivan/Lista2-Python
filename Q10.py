grafo = {}
while True:
    opcao = input("Deseja adicionar uma aresta? (s/n) ")
    if opcao == "s":
        aresta = input("Digite a aresta (ex: A-B): ")
        v1, v2 = aresta.split("-")
        if v1 not in grafo:
            grafo[v1] = set()
        if v2 not in grafo:
            grafo[v2] = set()
        grafo[v1].add(v2)
        grafo[v2].add(v1)
    else:
        break
print("Grafo atual:")
for v1 in grafo:
    for v2 in grafo[v1]:
        print(v1 + "-" + v2)
while True:
    opcao = input("Deseja remover uma aresta? (s/n) ")
    if opcao == "s":
        aresta = input("Digite a aresta a ser removida (ex: A-B): ")
        v1, v2 = aresta.split("-")
        if v1 in grafo and v2 in grafo[v1]:
            grafo[v1].remove(v2)
            grafo[v2].remove(v1)
        else:
            print("A aresta informada não existe no grafo!")
    else:
        break