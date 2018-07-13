import networkx as nx
import random
import matplotlib.pyplot as plt

def create_graph():
    g1 = nx.gnp_random_graph(100, 0.1)
    g2 = nx.gnp_random_graph(100, 0.05)
    mapping = dict(zip(g2.nodes(), range(100, 200)))
    g2 = nx.relabel_nodes(g2, mapping)
    n1 = random.sample(range(0, 100), 5)
    n2 = random.sample(range(100, 200), 5)
    bot_edges = list(zip(n1, n2))
    g = nx.compose(g1, g2)
    g.add_edges_from(bot_edges)
    nx.draw_spring(g, node_size=10)
    plt.savefig("graph.png")

create_graph()

