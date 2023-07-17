## Participantes:
### Lucas Morais Freire
### João Gabriel Rodrigues de Azevedo
### João Victor Moura Monteiro Madruga
- Breve apresentação sobre o projeto: [Loom](https://www.loom.com/share/e72574e73df74a15b791a9e4f3a21ff8)

Neste projeto, fizemos um Python Notebook que implementa um algoritmo de snowballing pela Wikipedia para montar um grafo que modela o caminho dos links entre os artigos, O código gera diversas vizualizações e gráficos que mostram diversas métricas. Para isso, foram utilizadas bibliotecas como Matplotlib, Pandas, Seaborn, networkx, nxviz e a própria biblioteca da Wikipedia. Também foi construída uma pipeline que gera todos estes dados automaticamente, com a instanciação de um objeto `Pipeline()` e chamando o método `.run(SEED, STOPS, n_layers)`, você pode escolher a página de início do algoritmo, as páginas a ignorar e a quantidade de camadas que serão permitidas.
