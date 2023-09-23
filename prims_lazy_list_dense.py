import random
import heapq

# define number of nodes
nodes = 10  #for 5000 nodes, it takes a huge time to create a graph, for demonstration i took 10 nodes only
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

# create minimum spanning tree
def lazy_prims(undirected_graph):
    mst = []
    # to mark whether a node is visited or not
    visited_nodes = [False for x in range(nodes)]
    heap = []
    start_vertex = 0
    for neighbor in undirected_graph[start_vertex]:
        heapq.heappush(heap,(neighbor[1],start_vertex,neighbor[0]))
    visited_nodes[start_vertex] = True
    while(len(heap) > 0):
        edge = heapq.heappop(heap)
        if visited_nodes[edge[2]] == True:
            continue
        else:
            visited_nodes[edge[2]] = True
            mst.append((edge[1],edge[2],edge[0]))
            for neighbor in undirected_graph[edge[2]]:
                if visited_nodes[neighbor[0]] == False:
                    heapq.heappush(heap,(neighbor[1],edge[2],neighbor[0]))
    return mst

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
    result = lazy_prims(graph_generated)
    print("\n\nMST Visualization\n")
    print_mst(result)


