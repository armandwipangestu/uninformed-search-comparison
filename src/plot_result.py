import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/runtime_results.csv")

plt.figure(figsize=(8, 5))
plt.plot(df["Nodes"], df["BFS (s)"], marker='o', label="BFS")
plt.plot(df["Nodes"], df["DFS (s)"], marker='o', label="DFS")
plt.plot(df["Nodes"], df["UCS (s)"], marker='o', label="UCS")

plt.title("Runtime Comparison of BFS, DFS, and UCS")
plt.xlabel("Number of Nodes")
plt.ylabel("Execution Time (seconds)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("results/runtime_chart.png")
plt.show()