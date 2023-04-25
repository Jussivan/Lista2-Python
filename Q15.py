grafo = {}
n = int(input("Digite o número de vértices do grafo: "))
for i in range(n):
    vertice = input(f"Digite o nome do vértice {i+1}: ")
    grafo[vertice] = []
m = int(input("Digite o número de arestas do grafo: "))
for i in range(m):
    aresta = input(f"Digite os vértices da aresta {i+1} separados por espaço: ")
    v1, v2 = map(str, aresta.split())
    grafo[v1].append(v2)
    grafo[v2].append(v1)
if 'A' in grafo and 'C' in grafo['A']:
    print("A aresta ('A', 'C') está presente no grafo")
else:
    print("A aresta ('A', 'C') não está presente no grafo")