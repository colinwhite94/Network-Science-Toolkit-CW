# Network-Science-Toolkit-CW
This is a toolkit of several network science functions that help analyze and get cursory information on a given network graph. Each function (there are 6) will take an edge list and return usefull informaiton for getting familiar with a new and graph. 

f1: Creates a NetworkX graph from an edge list and prints the number of nodes and edges.

f2: Creates a graph from an edge list and calculates the degree assortativity coefficient, which measures whether nodes with similar degrees tend to connect to each other.

f3: Creates a graph from an edge list and checks whether the graph is connected (if a path exists between every (any) pair of nodes.)

f4: Creates a graph from an edge list, finds its degree sequence, and creates a configuration model (a randomized graph with the same degree sequence as the original).

f5: Creates a graph from an edge list and calculates diameter, density, and average clustering coefficient.

f6: Creates a graph from an edge list and applies the Louvain algorithm to detect communities within the network.

These basic tools can be tedious to implement each time so it is helpful to have them quickly accessible via these pre made methods. 
