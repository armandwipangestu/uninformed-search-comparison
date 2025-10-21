import time
import pandas as pd
from graph_utils import generate_random_graph
from bfs import bfs
from dfs import dfs
from ucs import ucs

def measure_runtime(algorithm, graph, start, goal):
    start_time = time.time()
    result = algorithm(graph, start, goal)
    elapsed = time.time() - start_time
    return elapsed

def main():
    results = []
    sizes = [100, 500, 1000]

    for n in sizes:
        G = generate_random_graph(num_nodes=n, edge_prob=0.05)
        start, goal = 0, n - 1

        bfs_time = measure_runtime(bfs, G, start, goal)
        dfs_time = measure_runtime(dfs, G, start, goal)
        _, ucs_cost = ucs(G, start, goal)
        ucs_time = measure_runtime(lambda g, s, t: ucs(g, s, t)[0], G, start, goal)

        results.append({
            "Nodes": n,
            "BFS (s)": bfs_time,
            "DFS (s)": dfs_time,
            "UCS (s)": ucs_time,
        })

    df = pd.DataFrame(results)
    df.to_csv("results/runtime_results.csv", index=False)
    print(df)

if __name__ == "__main__":
    main()