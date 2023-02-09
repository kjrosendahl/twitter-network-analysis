import matplotlib.pyplot as plt
import networkx as nx

edges = []
id_dict = {} 
id_count = 0 

with open('users.txt', 'r') as f: 
    for line in f: 
        node, followers = line.split(sep='|')
        node = int(node)
        followers = followers.strip()
        followers = followers.strip('[')
        followers = followers.strip(']')
        list_followers = list(map(int, followers.split(',')))
        for follower in list_followers: 

            if node in id_dict: 
                node_id = id_dict[node]
            else: 
                node_id = id_count 
                id_dict[node] = node_id 
                id_count += 1 
            if follower in id_dict: 
                follower_id = id_dict[follower]
            else: 
                follower_id = id_count 
                id_dict[follower] = follower_id 
                id_count += 1 
            edges.append((node_id, follower_id, 1))

# edges are in list/container of 3-tuples (v1, v2, weight)
# edges = [(1,2,1), (2,1,2), (2,3,1), (3,4,2), (1,3,2)]

DG = nx.DiGraph()
DG.add_weighted_edges_from(edges)
plt.figure(1, figsize=(15, 15))

nx.draw(DG, with_labels=True, font_size = 2, width=.5, node_size = 20, arrowsize = 5) 
plt.savefig('network-graph.png')
plt.show()