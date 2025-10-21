import networkx as nx
import random

def generate_random_graph(num_nodes=100, edge_prob=0.1, weighted=True):
    G = nx.gnp_random_graph(num_nodes, edge_prob, directed=False)
    if weighted:
        for (u, v) in G.edges():
            G[u][v]['weight'] = random.randint(1, 10)
    return G