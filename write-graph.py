import matplotlib.pyplot as plt
import networkx as nx

def parse_network(file_name): 
    # initialize edge list
    edges = []

    # used to map complicated Twitter IDs to more readable IDs
    id_dict = {} 
    id_count = 0 

    # transform data file into an edge list 
    with open(file_name, 'r') as f: 
        for line in f: 

            # parse file 
            node, followers = line.split(sep='|')
            node = int(node)
            followers = followers.strip()
            followers = followers.strip('[')
            followers = followers.strip(']')
            list_followers = list(map(int, followers.split(',')))

            # add each follower as an in-neighbor of each node
            for follower in list_followers: 

                # assign unique ID to node 
                if node in id_dict: 
                    node_id = id_dict[node]
                else: 
                    node_id = id_count 
                    id_dict[node] = node_id 
                    id_count += 1 
                # assign unique ID to follower 
                if follower in id_dict: 
                    follower_id = id_dict[follower]
                else: 
                    follower_id = id_count 
                    id_dict[follower] = follower_id 
                    id_count += 1 

                # add edge from follower to node
                edges.append((follower_id, node_id, 1))

    return edges 

def draw_graph(graph): 

    # draw graph 
    plt.figure(1, figsize=(15, 15))
    nx.draw(graph, with_labels=True, font_size = 3, width=.5, node_size = 25, arrowsize = 7) 
    # save graph 
    plt.savefig('network-graph.png')
    plt.show()

def plot_degree_dist(graph): 

    deg_centrality = nx.in_degree_centrality(graph) 
    centrality_values = list(deg_centrality.values())

    plt.hist(centrality_values, bins=12)
    plt.xlabel('Degree Centrality')
    plt.ylabel('Frequency')
    plt.title('Frequency vs Degree Centrality')
    plt.savefig('degree-dist-hist.png')
    plt.show() 

def plot_closeness_dist(graph): 
    
    closeness_centrality = nx.closeness_centrality(graph)
    centrality_values = list(closeness_centrality.values())
    plt.hist(centrality_values, bins=8)
    plt.xlabel('Closeness Centrality')
    plt.ylabel('Frequency')
    plt.title('Frequency vs Closeness Centrality')
    plt.savefig('closeness-hist.png')
    plt.show() 

def plot_betweenness_dist(graph): 
    
    between_centrality = nx.betweenness_centrality(graph)
    centrality_values = list(between_centrality.values())
    plt.hist(centrality_values, bins=12)
    plt.xlabel('Betweenness Centrality')
    plt.ylabel('Frequency')
    plt.title('Frequency vs Betweenness Centrality')
    plt.savefig('betweenness-hist.png')
    plt.show() 

edges = parse_network('users.txt')
DG = nx.DiGraph() 
DG.add_weighted_edges_from(edges)
