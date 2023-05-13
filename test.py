import networkx as nx

def get_leaves(G:nx.Graph):
  L = []
  for node in G.nodes:
    if G.degree[node] == 1:
      L.append(node)
  return L

G = nx.Graph()
G.add_edges_from([
        ('a', 'b'),
        ('a', 'd'),
        ('c', 'd'),
    ])

print(get_leaves(G))