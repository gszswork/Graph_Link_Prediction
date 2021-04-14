import networkx as nx
import matplotlib.pyplot as plt
import random
from networkx.drawing.nx_pylab import draw_networkx
with open('edges.txt', 'r') as f:
    edges = f.readlines()
plt.figure(figsize=(30,20))
edge_tuple_list = []
for line in edges:
    line = line.strip()
    source, sink, _ = line.split(" ")
    if source != sink:
        edge_tuple_list.append((int(source), int(sink)))

#little_list = edge_tuple_list
little_list = random.sample(edge_tuple_list, 1000)

G = nx.Graph()
G.add_edges_from(little_list)

draw_networkx(G, edge_color='#6495ED',node_color='r', font_size=1, node_size=3)

#nx.draw(G,node_color = 'r',edge_color = 'b',with_labels = False,font_size =2,node_size =1)
plt.show()