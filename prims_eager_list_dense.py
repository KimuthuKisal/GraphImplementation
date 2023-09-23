import random
import sys

# define number of nodes
nodes = 10  #for 5000 nodes, it takes a huge time to create a graph, for demonstration i took 10 nodes only
random_val_begin = 1
random_val_end = 100

# define an empty graph
graph = {}

# to keep track of the minimum edge weights for each node in the graph
key = [sys.maxsize for x in range(nodes)]

# to mark whether a node is visited or not
visited_nodes = [False for x in range(nodes)]

# define nodes with no edges
def initialize_graph():
    for i in range( nodes ):
        graph[i] = []
    return graph

# create a graph using random edge weights
def generate_dense_graph():
    for i in range( nodes ):
        for j in range( i+1, nodes ):
            weight = random.randint( random_val_begin, random_val_end )
            graph[i].append( ( j, weight ) )
            graph[j].append( ( i, weight ) )
    return graph

# create minimum spanning tree
def prims_eagar(undirected_graph):
    mst = []
    visiting_graph = [-1 for x in range(nodes)]
    key[0] = 0
    for i in range(nodes):
        minimum_vertex = min_key_vertex(key,visited_nodes)
        visited_nodes[minimum_vertex] = True
        for neighbor in undirected_graph[minimum_vertex]:
            if visited_nodes[neighbor[0]] == False and neighbor[1] < key[neighbor[0]]:
                key[neighbor[0]] = neighbor[1]
                visiting_graph[neighbor[0]] = minimum_vertex
    for i in range(1,nodes):
        mst.append((visiting_graph[i],i,key[i]))
    return mst

# find the minimum key of  the vertex
def min_key_vertex(key,visited_nodes):
    minimum_key = sys.maxsize
    minimum_vertex = -1
    for i in range(nodes):
        if visited_nodes[i] == False and key[i] < minimum_key:
            minimum_key = key[i]
            minimum_vertex = i
    return minimum_vertex

# visualize the graph with weights
def print_graph(graph):
    for i in range(nodes):
        print(i, " => ", end="")
        for j in graph[i]:
            if ( j[0]==nodes-1 or ( i==nodes-1 and j[0]==nodes-2 ) ):
                print(j, end="")
            else:
                print(j, "-> ", end="")
        print("\n")

# visualize the mst
def print_mst(mst):
    for i in range(nodes):
        print(i, " => ", end="")
        for edge in mst:
            start_node, end_node, weight = edge
            if start_node==i:
                print(" (", end_node, ",", weight, ") ", end="")
        print("\n")
    
#main function
if '__main__' == __name__:
    graph_generated = initialize_graph()
    graph_generated = generate_dense_graph()
    print("\nGraph Visualization\n")
    print_graph(graph_generated)
    result = prims_eagar(graph_generated)
    print("\n\nMST Visualization\n")
    print_mst(result)


