import random
import numpy as np


def main():
    width, height = 33, 33
    maze = np.ones((width, height), dtype=int)
    maze[1::2, 1::2] = 0  # clear each room

    stack = [(1, 1)]

    visited = set()
    visited.add((1, 1))

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

    for y in range(height):
        line = ""
        for x in range(width):
            if maze[x, y] == 1:
                line += '# '
            else:
                line += '. '

        print(line)


if __name__ == "__main__":
    main()
