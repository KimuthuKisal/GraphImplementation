import random
import time

# define number of nodes
nodes = 100  #for 5000 nodes, it takes a huge time to create a graph, for demonstration i took 100 nodes only
random_val_begin = 1
random_val_end = 100

# define an empty graph
graph = {}

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

# check whether there exists a cycle if the relevant edge is added
def find_cycle( visiting_graph, node ):
    if visiting_graph[node] == -1:
        return node
    return find_cycle(visiting_graph, visiting_graph[node])

# mark the visited node in the visiting graph
def mark_visit( visiting_graph, start_node, end_node ):
    start_node_set = find_cycle( visiting_graph, start_node )
    end_node_set = find_cycle( visiting_graph, end_node )
    visiting_graph[start_node_set] = end_node_set

# create minimum spanning tree
def kruskal( undirected_graph ):

    edges = []
    for node in undirected_graph:
        for (adj_node, adj_weight) in undirected_graph[node]:

            # ( start_node, end_node, weight )
            edges.append( ( node, adj_node, adj_weight ) )      

    # sort the edge list using the weight
    edges.sort(key=lambda edge: edge[2])

    # define the minimum spanning tree 
    minimum_spanning_tree = []

    # define another list to track visited nodes
    visiting_graph = [-1]*nodes

    for edge in edges:
        start_node, end_node, adj_weight = edge

        # if both nodes are not visited, append to the minimum spanning tree
        if ( find_cycle( visiting_graph, start_node ) != find_cycle( visiting_graph, end_node ) ):
            # if a cycle is not going to be created, append the edge to the minimum spanning tree
            minimum_spanning_tree.append( ( start_node, end_node, adj_weight ) )
            # mark the visited node
            mark_visit( visiting_graph, start_node, end_node )
    return minimum_spanning_tree

# visualize the graph with weights
def print_graph(graph):
    for i in range(nodes):
        print(i, "=> ", end="")
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
if __name__ == '__main__':
    graph = initialize_graph()
    graph = generate_dense_graph()
    print("\nGraph Visualization\n")
    print_graph(graph)
    start_time = time.time()
    mst = kruskal(graph)
    end_time = time.time()
    time_range = end_time-start_time
    print("\n\nMST Visualization\n")
    print_mst(mst)
    print("\nTime Difference : ", time_range, "\n")
                