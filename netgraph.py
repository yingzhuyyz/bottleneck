import networkx as nx
import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def get_edge_color(g):
    edges = g.edges()
    weights = [g.edges[e]['weight'] for e in edges]
    maxw = max(weights)
    return [w*2/maxw for w in weights]
    
def draw_graph(g):
    weights = [g[u][v]['weight'] for u, v in g.edges()]
    pos = nx.spring_layout(g)
    cmap = plt.cm.get_cmap('Greys')
    nx.draw(g, 
            node_size=6, 
            edge_color = get_edge_color(g), 
            edge_cmap = cmap,
            pos=pos)
    plt.savefig("graph.png")

def create_graph():
    g1 = nx.gnp_random_graph(100, 0.1)
    g2 = nx.gnp_random_graph(100, 0.05)
    mapping = dict(zip(g2.nodes(), range(100, 200)))
    g2 = nx.relabel_nodes(g2, mapping)
    n1 = random.sample(range(0, 100), 2)
    n2 = random.sample(range(100, 200), 2)
    bot_edges = list(zip(n1, n2))
    g = nx.compose(g1, g2)
    g.add_edges_from(bot_edges)
    for x in list(g.edges()):
        g.edges[x]['weight'] = 1
    return g

def random_path(g):
    n1 = random.randint(0, 199)
    n2 = random.randint(0, 199)
    try:
        path = nx.shortest_path(g, n1, n2)
        for i in range(0, len(path)-1):
            g.edges[path[i], path[i+1]]['weight'] += 1
    except:
        pass
    return g

g = create_graph()
for i in range(1, 20):
    g = random_path(g)
draw_graph(g)

plt.cla()
plt.clf()
weights = [g.edges[e]['weight'] for e in g.edges()]
plt.hist(weights, 30)
plt.xlabel('weights')
plt.ylabel('number of edges')
plt.show()
