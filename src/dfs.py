def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited, path = set(), [start]
    visited.add(start)

    if start == goal:
        return path
    
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, goal, visited, path  + [neighbor])
            if new_path:
                return new_path
    return None