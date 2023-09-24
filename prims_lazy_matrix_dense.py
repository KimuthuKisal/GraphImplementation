import random
import heapq
import time

# define number of nodes
nodes = 100  #for 5000 nodes, it takes a huge time to create a graph, for demonstration i took 100 nodes only
random_val_begin = 1
random_val_end = 100

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
def prims_lazy(matrix):
    visited_nodes = [False for x in range(nodes)]
    mst = []
    visited_nodes[0] = True
    edges = []
    for i in range(nodes):
        if matrix[0][i] != 0:
            heapq.heappush(edges,(matrix[0][i],0,i))
    while(len(edges) != 0):
        edge = heapq.heappop(edges)
        if visited_nodes[edge[2]] == True:
            continue
        else:
            visited_nodes[edge[2]] = True
            mst.append(edge)

            for i in range(nodes):
                if matrix[edge[2]][i] != 0:
                    heapq.heappush(edges,(matrix[edge[2]][i],edge[2],i))
    return mst

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
        resultant_matrix[resultant_graph[i][1]][resultant_graph[i][2]] = resultant_graph[i][0]
        resultant_matrix[resultant_graph[i][2]][resultant_graph[i][1]] = resultant_graph[i][0]
    print_graph(resultant_matrix)

#main function
if '__main__' == __name__:
    adjacency_matrix = [[0 for i in range(nodes)] for j in range(nodes)]
    generated_adjacency_matrix = generate_dense_graph(adjacency_matrix)
    print("\nGraph Visualization\n")
    print_graph(generated_adjacency_matrix)
    start_time = time.time()
    mst = prims_lazy(generated_adjacency_matrix)
    end_time = time.time()
    time_range = end_time-start_time
    print("\n\nMST Visualization\n")
    print_resultant_mst(mst)
    print("\nTime Difference : ", time_range, "\n")

    