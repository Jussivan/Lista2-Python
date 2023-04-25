grafo = {}
vertices = input("Digite os vértices do grafo, separados por espaço: ").split()
for v in vertices:
    grafo[v] = []
arestas = input("Digite as arestas do grafo, no formato 'vertice1 vertice2', separadas por vírgula: ").split(",")
for aresta in arestas:
    v1, v2 = aresta.split()
    grafo[v1].append(v2)
    grafo[v2].append(v1)
print("Grafo:", grafo)