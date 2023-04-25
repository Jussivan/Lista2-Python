grafo = {}
vertices = input("Insira os vértices do grafo separados por espaço: ").split()
for vertice in vertices:
    grafo[vertice] = []
arestas = input("Insira as arestas do grafo separadas por espaço (ex: 'A B'): ").split()
for aresta in arestas:
    v1, v2 = aresta.split()
    grafo[v1].append(v2)
    grafo[v2].append(v1)
print("Grafo:")
for vertice, adjacentes in grafo.items():
    print(vertice + " -> " + ", ".join(adjacentes))