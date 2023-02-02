import matplotlib.pyplot as plt
import networkx as nx

# edges are in list/container of 3-tuples (v1, v2, weight)
edges = [(1,2,1), (2,1,2), (2,3,1), (3,4,2), (1,3,2)]

DG = nx.DiGraph()
DG.add_weighted_edges_from(edges)
nx.draw(DG, with_labels=True) 
plt.show()