import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.community import louvain_communities

def add_num(a: int, b: int) -> int: #testing function
    return a + b

#edge_list = [(1,2), (3,5), (9,4), (4,7)] #test edge list
#edge_list = [(2, 1), (3, 1), (3, 2), (4, 1), (4, 2), (4, 3), (5, 1), (6, 1), (7, 1), (7, 5), (7, 6), (8, 1), (8, 2), (8, 3), (8, 4), (9, 1), (9, 3), (10, 3), (11, 1), (11, 5), (11, 6), (12, 1), (13, 1), (13, 4), (14, 1), (14, 2),  (14, 3), (14, 4), (17, 6), (17, 7), (18, 1), (18, 2), (20, 1), (20, 2), (22, 1), (22, 2), (26, 24), (26, 25), (28, 3), (28, 24), (28, 25), (29, 3), (30, 24), (30, 27), (31, 2), (31, 9), (32, 1), (32, 25), (32, 26), (32, 29), (33, 3), (33, 9), (33, 15), (33, 16), (33, 19), (33, 21), (33, 23), (33, 24), (33, 30), (33, 31), (33, 32), (34, 9), (34, 10), (34, 14), (34, 15), (34, 16), (34, 19), (34, 20), (34, 21), (34, 23), (34, 24), (34, 27), (34, 28), (34, 29), (34, 30), (34, 31), (34, 32), (34, 33)] #karate club graph edge list as test

def f1(edge_list: list) -> list:
    graph = nx.Graph()
    graph.add_edges_from(edge_list)
    a = "Number of nodes: %d" % graph.number_of_nodes()
    b = "Number of edges: %d" % graph.number_of_edges()
    return print("\n",a,"\n", b)

def f2(edge_list: list) -> list:
    graph = nx.Graph()
    graph.add_edges_from(edge_list)
    asort = nx.degree_assortativity_coefficient(graph, x='out', y='in', weight=None, nodes=None)
    return print("Degree assortativity coefficient:", asort)

def f3(edge_list: list) -> list:
    graph = nx.Graph()
    graph.add_edges_from(edge_list)
    return print("The graph is connected",nx.is_connected(graph))

def f4(edge_list: list) -> list:
    graph = nx.Graph()
    graph.add_edges_from(edge_list)
    deg_sequence = [d for n, d in graph.degree()]
    graph_config = nx.configuration_model(deg_sequence, create_using=None, seed=None)
    return print("Configuration model applied as graph_config"),graph_config

def f5(edge_list: list) -> list:
    graph = nx.Graph()
    graph.add_edges_from(edge_list)
    diameter = nx.diameter(graph)
    density = nx.density(graph)
    clustering_coefficient = nx.average_clustering(graph)
    return  print("diameter", diameter, "\n", "density", density, "\n", "clustering_coefficient", clustering_coefficient, "\n")

def f6(edge_list: list) -> list:
    G = nx.Graph()
    G.add_edges_from(edge_list)
    com = louvain_communities(G, weight='weight', resolution=1, threshold=1e-07, max_level=None, seed=None)
    return print("Louvain communities:", com, "\n")

# f1(edge_list)
# f2(edge_list)
# f3(edge_list)           
# f4(edge_list)
# f5(edge_list)
# f6(edge_list) 