from subtask1 import G, ST


def dfs_paths(graph, start, goal, path=[]):
    path = path + [start]
    if start == goal:
        return [path]
    if start not in graph:
        return []
    paths = []
    for neighbor in graph[start]:
        if neighbor not in path:
            new_paths = dfs_paths(graph, neighbor, goal, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (node, path) = queue.pop(0)
        for next_node in set(graph[node]) - set(path):
            if next_node == goal:
                yield path + [next_node]
            else:
                queue.append((next_node, path + [next_node]))


if __name__ == '__main__':
    # Отримання списку всіх можливих шляхів між вершинами 1 і 4 за допомогою DFS і BFS
    a, b = ST.GEIN, ST.NOORD
    dfs_all_paths = list(dfs_paths(G, a, b))
    bfs_all_paths = list(bfs_paths(G, a, b))

    print("Шляхи з використанням DFS:", dfs_all_paths)
    print("Шляхи з використанням BFS:", bfs_all_paths)
