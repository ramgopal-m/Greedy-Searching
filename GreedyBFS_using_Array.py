import numpy as np # type: ignore

adj_matrix = np.array([
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # S
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],  # A
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],  # B
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # C
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # D
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # E
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],  # F
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # H
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # I
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # G
])

heuristic = {'S': 13, 'A': 12, 'B': 4, 'C': 7, 'D': 3, 'E': 8, 'F': 2, 'G': 0, 'H': 4, 'I': 9}

node_to_index = {'S': 0, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'H': 7, 'I': 8, 'G': 9}
index_to_node = {v: k for k, v in node_to_index.items()}


def greedy_best_first_search(start, goal):
    open_list = [(start, heuristic[start])]
    visited = set()
    path = []

    while open_list:
        open_list.sort(key=lambda x: x[1]) 
        current, _ = open_list.pop(0)
        path.append(current)
        visited.add(current)

        if current == goal:
            return path

        current_index = node_to_index[current]
        neighbors = [index_to_node[i] for i in range(len(adj_matrix[current_index])) if adj_matrix[current_index][i] == 1]

        for neighbor in neighbors:
            if neighbor not in visited and neighbor not in [n[0] for n in open_list]:
                open_list.append((neighbor, heuristic[neighbor]))

    return path

result_path = greedy_best_first_search('S', 'G')
print(" -> ".join(result_path))
