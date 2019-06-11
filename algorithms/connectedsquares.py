import numpy as np

grid = [[0, 0, 1, 2],
        [0, 1, 2, 1],
        [2, 1, 1, 1]]

visited = set()

def get_num_connected_nodes():
    max_len = 0
    item = 0

    for i in range(3):
        for j in range(4):
            if not visited.__contains__((i,j)):
                num_connected_nodes = dfs((i, j))
                if num_connected_nodes > max_len:
                    max_len = num_connected_nodes
                    item = grid[i][j]
    return item, max_len

def dfs(loc):
    visited.add(loc)
    stack = []
    stack.append(loc)
    max_len = 1
    while len(stack) !=0:
        loc = stack.pop()
        neighbours = get_neighbours(loc)
        for locs in neighbours:
            if not visited.__contains__(locs):
                visited.add(locs)
                stack.append(locs)
                max_len += 1

    return max_len

def get_neighbours(loc):
    neighbours = []
    row, col = loc
    item = grid[row][col]
    if row-1>=0:
        if item==grid[row-1][col]:
            neighbours.append((row-1, col))
    if row+1<3:
        if item==grid[row+1][col]:
            neighbours.append((row+1, col))
    if col-1>=0:
        if item==grid[row][col-1]:
            neighbours.append((row, col-1))
    if col+1<4:
        if item==grid[row][col+1]:
            neighbours.append((row, col+1))

    return neighbours

if __name__ == '__main__':
    print(get_num_connected_nodes())
