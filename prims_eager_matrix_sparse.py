import random
import sys

# define number of nodes
nodes = 10  #for 5000 nodes, it takes a huge time to create a graph, for demonstration i took 10 nodes only
random_val_begin = 1
random_val_end = 100

# to keep track of the minimum edge weights for each node in the graph
key = [sys.maxsize for x in range(nodes)]

# to mark whether a node is visited or not
visited_nodes = [False for x in range(nodes)]

# create a graph using random edge weights
def generate_random_tree(matrix,i):
    while(True):
        if i == nodes - 1:
            break
        else:
            j = random.randint(0,nodes-1)
            weight = random.randint(random_val_begin,random_val_end)
            if j == i:
                continue
            else:
                if matrix[i][j] == 0:
                    matrix[i][j] = weight
                    matrix[j][i] = weight
                    i = i + 1
                else:
                    continue 
    return matrix

# add a random edge with random weight to the graph
def add_edges(matrix,n):
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
                if matrix[i][j] == 0:
                    matrix[i][j] = weight
                    matrix[j][i] = weight
                    n = n - 1
                else:
                    continue
    return matrix

# create a sparse graph using random edge weights
def generate_sparse_graph(matrix,i):
    matrix = generate_random_tree(matrix,i)
    extra_no_of_edges = nodes//2
    matrix = add_edges(matrix,extra_no_of_edges)
    return matrix

# create minimum spanning tree
def eagar_prims(matrix,start_vertex = 0):
    key[start_vertex] = 0
    parent = [-1 for x in range(nodes)]
    mst = []
    for _ in range(nodes):
        start_node = min_key_vertex()
        visited_nodes[start_node] = True
        for end_node in range(nodes):
            if matrix[start_node][end_node] != 0 and visited_nodes[end_node] == False and matrix[start_node][end_node] < key[end_node]:
                parent[end_node] = start_node
                key[end_node] = matrix[start_node][end_node]
    for i in range(1,nodes):
        mst.append((parent[i],i,matrix[i][parent[i]]))
    return mst

# find the minimum key of  the vertex
def min_key_vertex():
    min = sys.maxsize
    min_vertex = -1
    for i in range(nodes):
        if visited_nodes[i] == False and key[i] < min:
            min = key[i]
            min_vertex = i
    return min_vertex

# visualize the graph with weights
def print_graph(matrix):
    print("\t", end="")
    for i in range(nodes):
        print(i, "\t", end="")
    print("\n")
    for i in range(nodes):
        print(i, " =>\t", end="")
        for j in range(nodes):
            print(matrix[i][j],"\t", end="")
        print("\n")

# visualize the resultant graph with weights
def print_resultant_mst(resultant_graph):
    resultant_matrix = [[0 for x in range(nodes)] for y in range(nodes)]
    for i in range(len(resultant_graph)):
        resultant_matrix[resultant_graph[i][0]][resultant_graph[i][1]] = resultant_graph[i][2]
        resultant_matrix[resultant_graph[i][1]][resultant_graph[i][0]] = resultant_graph[i][2]
    print_graph(resultant_matrix)


if '__main__' == __name__:
    adjacency_matrix = [[0 for x in range(nodes)] for y in range(nodes)]
    generated_adjacency_matrix = generate_sparse_graph(adjacency_matrix,0)
    print("\nGraph Visualization\n")
    print_graph(generated_adjacency_matrix)
    mst = eagar_prims(generated_adjacency_matrix)
    print("\n\nMST Visualization\n")
    print_resultant_mst(mst)



