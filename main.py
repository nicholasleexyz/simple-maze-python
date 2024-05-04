import random
import numpy as np


def main():
    width, height = 16, 16
    maze = np.ones((width, height), dtype=int)
    maze[1::2, 1::2] = 0  # clear each room

    stack = [(0, 0)]

    visited = set()
    visited.add((0, 0))

    while stack:
        current = stack[-1]
        directions = {(0, -2), (2, 0), (0, 2), (-2, 0)}

        potential_neighbors = [
            (current[0] + _direction[0], current[1] + _direction[1])
            for _direction in directions]

        valid_neighbors = [n for n in potential_neighbors
                           if 0 <= n[0] < width and 0 <= n[1] < height]

        unvisited = [vn for vn in valid_neighbors if vn not in visited]

        if unvisited:
            neighbor = random.choice(unvisited)
            wall = ((current[0] + neighbor[0]) // 2,
                    (current[1] + neighbor[1]) // 2)
            maze[wall[0], wall[1]] = 0
            visited.add(neighbor)
            stack.append(neighbor)
        else:
            stack.pop()

    scale = 3
    scaled_maze = np.kron(maze, np.ones((scale, scale), dtype=int))

    for y in range(height * scale):
        line = ""
        for x in range(width * scale):
            if (0 < x and scaled_maze[x - 1, y] == 0) or \
                    (0 < y and scaled_maze[x, y - 1] == 0) or \
                    (x < width * scale - scale and scaled_maze[x + scale - 2, y] == 0) or \
                    (y < height * scale - scale and scaled_maze[x, y + scale - 2] == 0) and \
                    scaled_maze[x, y] == 1:
                line += '. '
            else:
                line += '# '

        print(line)


if __name__ == "__main__":
    main()
