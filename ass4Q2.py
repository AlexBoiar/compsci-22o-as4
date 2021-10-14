#Assignment4
graphs_input = []
num_nodes = int(input())

while(num_nodes!=0):
    graph_1 = []
    for i in range(num_nodes):
        li = [int(weight) for weight in input().split()]
        graph_1+=[li]
    graphs_input+=[graph_1]
    num_nodes = int(input())


for graph_1 in graphs_input:
    nodes = len(graph_1)
    visited_towns = [x*0 for x in range(nodes)]
    visited_towns[0] = True
    visited = 0
    tot_cost=0
    while(visited<nodes-1):
        min_cost = 999999
        a_min=b_min=0
        for i in range(nodes):
            if visited_towns[i]:
                for j in range(nodes):
                    if ((not visited_towns[j]) and graph_1[i][j]):
                        if min_cost > graph_1[i][j]:
                            min_cost = graph_1[i][j]
                            a_min=i
                            b_min=j
        tot_cost+=graph_1[a_min][b_min]
        visited_towns[b_min] = True
        visited += 1
    print(tot_cost)
