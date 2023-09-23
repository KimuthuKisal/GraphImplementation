import random
import heapq

# define number of nodes
nodes = 10  #for 5000 nodes, it takes a huge time to create a graph, for demonstration i took 10 nodes only
random_val_begin = 1
random_val_end = 100

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
    adjacency_matrix = [[0 for x in range(nodes)] for y in range(nodes)]
    generated_adjacency_matrix = generate_sparse_graph(adjacency_matrix,0)
    print("\nGraph Visualization\n")
    print_graph(generated_adjacency_matrix)
    mst = prims_lazy(generated_adjacency_matrix)
    print("\n\nMST Visualization\n")
    print_resultant_mst(mst)
    



