import random

# define number of nodes
nodes = 10  #for 5000 nodes, it takes a huge time to create a graph, for demonstration i took 10 nodes only
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

# check whether there exists a cycle if the relevant edge is added
def find_cycle( visiting_graph, node ):
    if visiting_graph[node] == -1:
        return node
    return find_cycle(visiting_graph, visiting_graph[node])
    
# mark the visited node in the visiting graph
def mark_visit(visiting_graph,start_node,end_node):
    start_node_set = find_cycle(visiting_graph, start_node)
    end_node_set = find_cycle(visiting_graph,end_node)
    visiting_graph[start_node_set] = end_node_set

# create minimum spanning tree
def kruskal(matrix):
    resultant_graph = []
    i = 0
    e = 0
    visiting_graph = [-1 for x in range(nodes)]
    while e < nodes - 1:
        min = 999
        for i in range(nodes):
            for j in range(nodes):
                if find_cycle(visiting_graph,i) != find_cycle(visiting_graph,j) and matrix[i][j] < min and matrix[i][j] != 0:
                    min = matrix[i][j]
                    x = i
                    y = j
        mark_visit(visiting_graph,x,y)
        resultant_graph.append([x,y,matrix[x][y]])
        e = e + 1
    return resultant_graph

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
    adjacency_matrix = [[0 for i in range(nodes)] for j in range(nodes)]
    generated_adjacency_matrix = generate_dense_graph(adjacency_matrix)
    print("\nGenerated graph\n")
    print_graph(generated_adjacency_matrix)
    result = kruskal(generated_adjacency_matrix)
    print("\nResultant graph\n")
    print_resultant_mst(result)