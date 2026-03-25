from itertools import permutations

def tsp(graph):
    n = len(graph)
    nodes = list(range(n))
    min_path = float('inf')

    for perm in permutations(nodes[1:]):
        cost = 0
        k = 0
        for j in perm:
            cost += graph[k][j]
            k = j
        cost += graph[k][0]
        min_path = min(min_path, cost)

    return min_path
