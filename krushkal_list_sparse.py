import random

# define number of nodes
nodes = 10  #for 5000 nodes, it takes a huge time to create a graph, for demonstration i took 10 nodes only
random_val_begin = 1
random_val_end = 100

# define an empty graph
graph = {}

# define nodes with no edges
def initialize_graph():
    for i in range(nodes):
        graph[i] = []
    return graph

# create a graph using random edge weights
def generate_sparse_graph():
    i = 0
    while(True):
        if i == nodes:
            break
        else:
            j = random.randint(0,nodes-1)
            weight = random.randint(random_val_begin,random_val_end)
            if j == i:
                continue
            else:
                if j in graph[i]:
                    continue
                else:
                    graph[i].append((j,weight))
                    graph[j].append((i,weight))
                    i += 1
    return graph

# add a random edge with random weight to the graph
def add_edges(n):
    while(True):
        if n == 0:
            break
        else:
            i = random.randint(0,nodes-1)
            j = random.randint(0,nodes-1)
            weight = random.randint(random_val_begin,random_val_end)
            if i == j:
                continue
            else:
                if j in graph[i]:
                    continue
                else:
                    graph[i].append((j,weight))
                    graph[j].append((i,weight))
                    n -= 1
    return graph

# check whether there exists a cycle if the relevant edge is added
def find_cycle(visiting_graph, node):
    if visiting_graph[node] == -1:
        return node
    return find_cycle(visiting_graph, visiting_graph[node])

# mark the visited node in the visiting graph
def mark_visit(visiting_graph,start_node,end_node):
    start_node_set = find_cycle(visiting_graph,start_node)
    end_node_set = find_cycle(visiting_graph,end_node)
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
    print("\nGraph Visualization\n")
    for i in range(nodes):
        print(i, end="")
        for j in graph[i]:
            print(" -> ", j, end="")
        print("\n")

# visualize the mst
def print_mst(mst):
    print("\n\nMST Visualization\n")
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
    graph_generated = generate_sparse_graph()
    extra_no_of_edges = nodes//2
    graph_generated = add_edges(extra_no_of_edges)
    print_graph(graph)
    mst = kruskal(graph)
    print_mst(mst)


