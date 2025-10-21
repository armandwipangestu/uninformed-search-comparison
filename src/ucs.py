import heapq

def ucs(graph, start, goal):
    visited = set()
    pq = [(0, start, [start])]

    while pq:
        cost, node, path = heapq.heappop(pq)
        if node == goal:
            return path, cost
        if node not in visited:
            visited.add(node)
            for neighbor in graph.neighbors(node):
                weight = graph[node][neighbor].get('weight', 1)
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))
    return None, float('inf')