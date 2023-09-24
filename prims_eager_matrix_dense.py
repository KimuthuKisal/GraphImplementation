import random
import sys
import time

# define number ofnodes 
nodes = 100  #for 5000 nodes, it takes a huge time to create a graph, for demonstration i took 100 nodes only
random_val_begin = 1
random_val_end = 100

# to keep track of the minimum edge weights for each node in the graph
key = [sys.maxsize for x in range(nodes)]

# to mark whether a node is visited_nodes or not
visited_nodes = [False for x in range(nodes)]

# create a graph using random edge weights
def generate_dense_graph(matrix):
    for i in range(nodes):
        for j in range(nodes):
            if i == j:
                continue
            else:
                weight = random.randint(random_val_begin,random_val_end)
                matrix[i][j] = weight
                matrix[j][i] = weight
    return matrix

# create minimum spanning tree
def eagar_prims(matrix,start_vertex = 0):
    key[start_vertex] = 0
    parent = [-1 for x in range(nodes)]
    mst = []
    for i in range(nodes):
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

#main function
if '__main__' == __name__:
    adjacency_matrix = [[0 for x in range(nodes)] for y in range(nodes)]
    generated_adjacency_matrix = generate_dense_graph(adjacency_matrix)
    print("\nGraph Visualization\n")
    print_graph(generated_adjacency_matrix)
    start_time = time.time()
    mst = eagar_prims(generated_adjacency_matrix)
    end_time = time.time()
    time_range = end_time-start_time
    print("\n\nMST Visualization\n")
    print_resultant_mst(mst)
    print("\nTime Difference : ", time_range, "\n")



