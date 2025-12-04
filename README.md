# Sobre📌
Este projeto tem como propósito principal demonstrar e entender a função essencial dos Grafos na ciência da computação e na resolução de problemas práticos.
A classe implementada em Python modela um Grafo Ponderado, que é a representação ideal para qualquer rede onde as conexões têm um custo associado, como as distâncias 
em um mapa de estradas ou o tempo de transmissão em uma rede de computadores.

O código permite a construção dessa rede através de operações básicas: a criação de vértices (os pontos ou locais, como cidades) e a adição de arestas
(as ligações entre esses pontos, com um peso que representa o custo ou a distância). No entanto, o ponto alto do projeto e sua principal funcionalidade avançada é a aplicação do Algoritmo de Dijkstra.

## * Problema e Solução
### Problema:
O problema consiste em representar um conjunto de cidades (vértices) e suas conexões (arestas) com distâncias (pesos) entre elas, de forma a permitir a manipulação dinâmica da estrutura.
Isso inclui operações básicas como adicionar e remover vértices e arestas, além de uma operação avançada para calcular a rota mais curta entre duas cidades. A representação deve ser eficiente e
flexível, permitindo tanto grafos direcionados quanto não direcionados, e deve ser implementada em Python, garantindo clareza, organização e legibilidade do código.

### Solução
Para resolver o problema, foi implementada uma classe Grafo que utiliza uma lista de adjacência por meio de um dicionário. Essa escolha proporciona uma representação intuitiva e eficiente,
especialmente para grafos esparsos, que é comum em cenários como mapas de cidades. A classe oferece operações completas para manipulação do grafo: adição e remoção de vértices, 
adição e remoção de arestas (com suporte a pesos e direcionamento opcional), e exibição clara da estrutura.
Além disso, foi implementado o algoritmo de Dijkstra para cálculo do menor caminho entre dois vértices, considerando pesos não negativos.
O código foi organizado em dois arquivos: grafo.py, contendo a definição da classe com todos os métodos, e main.py, contendo exemplos demonstrativos e um menu interativo.
Essa separação garante modularidade, reusabilidade e facilidade de teste, atendendo aos requisitos mínimos e avançados solicitados.

## 🛠Como Executar?
Para executar o projeto, basta clonar o repositório para sua máquina local e abrir na IDE de sua preferência.
O desenvolvimento foi realizado no VS Code, mas qualquer ambiente compatível com Python 3 funciona corretamente.
Após clonar, você deve manter os arquivos organizados em pastas separadas (por exemplo: grafos.py e main.py), 
garantindo que ambos estejam no mesmo diretório para que o programa funcione. Em seguida, é possível rodar o código diretamente pela IDE.
### Clonar o repositório
Abra o terminal e execute: git clone https://github.com/SEU-USUARIO/seu-repositorio.git
### Abrir o projeto na IDE
* PyCharm
* VSCode (IDE utilizada no desenvolvimento)
* Thonny, Spyder, etc.
### Estrutura recomendada
* Abra o projeto em sua IDE (VS Code recomendado).
* Certifique-se de que grafos.py e main.py estão na mesma pasta.
* Execute o arquivo main.py pelo terminal integrado ou pelo botão Run.

### 📥 Exemplo de Entrada
O arquivo main.py cria quatro cidades e as liga por estradas com pesos
`````
g.adicionar_vertice("São Paulo")
g.adicionar_vertice("Rio de Janeiro")
g.adicionar_vertice("Belo Horizonte")
g.adicionar_vertice("Curitiba")


g.adicionar_aresta("São Paulo", "Rio de Janeiro", 430)
g.adicionar_aresta("São Paulo", "Belo Horizonte", 590)
g.adicionar_aresta("São Paulo", "Curitiba", 408)
g.adicionar_aresta("Rio de Janeiro", "Curitiba", 840)
`````

### 📤 Exemplo de Saída
`````
=GRAFO=
São Paulo -> Rio de Janeiro (peso=430), Belo Horizonte (peso=590), Curitiba (peso=408)
Rio de Janeiro -> São Paulo (peso=430), Curitiba (peso=840)
Belo Horizonte -> São Paulo (peso=590)
Curitiba -> São Paulo (peso=408), Rio de Janeiro (peso=840)

Menor caminho: ['Curitiba', 'São Paulo', 'Belo Horizonte']
Distância total: 998 km
`````
## ✔️ Requisitos Mínimos Implementados
* Representação do grafo com lista de adjacência
* Adicionar vértice
* Adicionar aresta (não direcionada, representando vias bidirecionais)
* Remover vértice
* Remover aresta
* Exibição textual do grafo
* Caso de uso: mapa de cidades e suas distâncias
### ⭐ Requisito Avançado Implementado
* Algoritmo de Dijkstra para encontrar o menor caminho entre duas cidades

### 🐍 Linguagem Utilizada
* Python 3.10+ (qualquer versão ≥ 3.8 funciona)
