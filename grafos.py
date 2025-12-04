import heapq

class Grafo:
    def __init__(self):
        # Aqui eu crio a estrutura do grafo.
        # Vou usar um dicionário onde cada chave é um vértice
        # e o valor é uma lista de (vizinho, peso).
        self.adjacencia = {}

    
    # Adicionar Vertice
    def adicionar_vertice(self, vertice):
        # Se o vértice ainda não existe, eu crio ele com uma lista vazia
        if vertice not in self.adjacencia:
            self.adjacencia[vertice] = []
        else:
            print(f"O vértice '{vertice}' já existe no grafo.")

   
    # Adicionar Aresta
    def adicionar_aresta(self, v1, v2, peso=1, direcionado=False):
        # Se os vértices não existirem, eu adiciono antes
        if v1 not in self.adjacencia:
            self.adicionar_vertice(v1)
        if v2 not in self.adjacencia:
            self.adicionar_vertice(v2)

        # Aqui adiciono a aresta v1 -> v2
        self.adjacencia[v1].append((v2, peso))

        # Se o grafo não for direcionado, crio a volta v2 -> v1
        # Nesse trabalho eu escolhi deixar como NÃO direcionado,
        # porque é mais fácil de representar mapas (meu caso de uso).
        if not direcionado:
            self.adjacencia[v2].append((v1, peso))


    # Remover Vertice
    def remover_vertice(self, vertice):
        if vertice in self.adjacencia:

            # Primeiro removo o vértice da lista dos vizinhos dos outros
            for v in self.adjacencia:
                self.adjacencia[v] = [(viz, p) for (viz, p) in self.adjacencia[v] if viz != vertice]

            # Agora removo ele do dicionário principal
            del self.adjacencia[vertice]

        else:
            print(f"Não existe o vértice '{vertice}' no grafo.")


    # Remover Aresta
    def remover_aresta(self, v1, v2, direcionado=False):
        # Removo v1 -> v2
        if v1 in self.adjacencia:
            self.adjacencia[v1] = [(viz, p) for (viz, p) in self.adjacencia[v1] if viz != v2]

        # Se não for direcionado, removo o contrário também
        if not direcionado and v2 in self.adjacencia:
            self.adjacencia[v2] = [(viz, p) for (viz, p) in self.adjacencia[v2] if viz != v1]

    # Exibir Grafos 
    def exibir(self):
        print("=GRAFO=")
        for vertice, vizinhos in self.adjacencia.items():
            # Aqui eu transformo a lista de tuplas em texto
            texto_vizinhos = ", ".join([f"{v} (peso={p})" for v, p in vizinhos])
            print(f"{vertice} -> {texto_vizinhos}")
        print("")


    # Dijkstra
    def dijkstra(self, inicio):
        # Aqui eu crio um dicionário que guarda a distância mínima até cada vértice
        # Começo tudo com infinito, menos o início
        dist = {v: float('inf') for v in self.adjacencia}
        dist[inicio] = 0

        # Para reconstruir o caminho depois
        anterior = {v: None for v in self.adjacencia}

        # Fila de prioridades: (distância, vértice)
        fila = [(0, inicio)]

        # Loop principal do Dijkstra
        while fila:
            dist_atual, atual = heapq.heappop(fila)

            # Se já temos algo melhor registrado, skip
            if dist_atual > dist[atual]:
                continue

            # Percorre os vizinhos
            for vizinho, peso in self.adjacencia[atual]:
                nova_dist = dist_atual + peso

                # Se a nova distância for melhor, eu atualizo
                if nova_dist < dist[vizinho]:
                    dist[vizinho] = nova_dist
                    anterior[vizinho] = atual
                    heapq.heappush(fila, (nova_dist, vizinho))

        return dist, anterior

    # Função para reconstruir o caminho final (usando o "anterior")
    def menor_caminho(self, inicio, fim):
        dist, anterior = self.dijkstra(inicio)

        # Se não tem caminho possível
        if dist[fim] == float('inf'):
            return None, float('inf')

        caminho = []
        atual = fim
        # Volto reconstruindo o caminho ao contrário
        while atual is not None:
            caminho.append(atual)
            atual = anterior[atual]

        caminho.reverse()  # Inverte porque estava ao contrário
        return caminho, dist[fim]

