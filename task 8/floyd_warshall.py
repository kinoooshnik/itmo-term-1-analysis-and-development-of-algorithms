import random
import sys

import networkx as nx
import numpy as np
from memory_profiler import profile


def generate_graph(n):
    m = (n * (n - 1)) // 2
    weight_range = (3, 10)
    matrix = np.zeros((n, n), dtype=int)
    edges = 0
    while edges < m:
        a = random.randint(0, n - 1)
        b = random.randint(0, n - 1)
        if a == b or matrix[a, b] != 0:
            continue
        weight = random.randint(*weight_range)
        matrix[a, b] = weight
        matrix[b, a] = weight
        edges += 1
    G = nx.from_numpy_matrix(matrix)
    return G


def floyd_warshall(G):
    return nx.floyd_warshall(G, weight="weight")


@profile
def main(n: int):
    G = generate_graph(n)
    floyd_warshall(G)


if __name__ == '__main__':
    n = int(sys.argv[1])
    main(n)
