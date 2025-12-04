from grafos import Grafo
import heapq   # vou usar isso no Dijkstra para a fila de prioridade

# Criando o grafo
g = Grafo()

# Adicionando algumas cidades (meu tema)
g.adicionar_vertice("São Paulo")
g.adicionar_vertice("Rio de Janeiro")
g.adicionar_vertice("Belo Horizonte")
g.adicionar_vertice("Curitiba")

# Adicionando as conexões com pesos (distâncias)
g.adicionar_aresta("São Paulo", "Rio de Janeiro", 430)
g.adicionar_aresta("São Paulo", "Belo Horizonte", 590)
g.adicionar_aresta("São Paulo", "Curitiba", 408)
g.adicionar_aresta("Curitiba", "Rio de Janeiro", 840)

# Exibindo o grafo
g.exibir()

# Testando o Dijkstra
caminho, distancia = g.menor_caminho("Curitiba", "Belo Horizonte")
print("Menor caminho:", caminho)
print("Distância total:", distancia, "km")
import heapq   # vou usar isso no Dijkstra para a fila de prioridade