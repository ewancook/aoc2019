from collections import defaultdict
from intcode import parse_intcode
from pathfinding import path_find

x_dirs = [0, 0, -1, 1]
y_dirs = [1, -1, 0, 0]


def vec_from_dir(last_move, pos):
    return (pos[0] + x_dirs[last_move - 1], pos[1] + y_dirs[last_move - 1])


def next_direction(dir, directions, reverse=False):
    i = directions.index(dir)
    a = -1 if reverse else 1
    return directions[(i + a) % len(directions)]


def walk_maze(code, directions):
    x, y = 0, 0
    last = directions[0]
    args = [last]
    maze = defaultdict(str, {})
    for status in parse_intcode(code, args):
        new_pos = vec_from_dir(last, (x, y))
        if not status:
            maze[new_pos] = "#"
            last = next_direction(last, directions)
        elif int(status) == 1:
            x, y = new_pos
            new_dir = next_direction(last, directions, reverse=True)
            if maze[vec_from_dir(new_dir, new_pos)] != "#":
                last = new_dir
        else:
            maze[new_pos] = "O"
            return maze, new_pos
        args.append(last)


def neighbours(maze, vec):
    for x, y in zip(x_dirs, y_dirs):
        new = (vec[0] + x, vec[1] + y)
        if not maze[new] == "#":
            yield new


def heuristic(vec, goal):
    return abs(vec[0] - goal[0]) + abs(vec[1] - goal[1])


def part_one(maze, goal):
    return path_find((0, 0), goal, maze, heuristic, neighbours)


def part_two(maze, goal):
    i, left = 0, [[goal]]
    while True:
        minute, to_add = left.pop(0), []
        for pos in minute:
            for n in neighbours(maze, pos):
                if maze[n] != "O":
                    maze[n] = "O"
                    to_add.append(n)
        if not to_add:
            return i
        left.append(to_add)
        i += 1


code = [int(i) for i in open("input.txt").readline().strip().split(",")]

first, goal = walk_maze(code[:], [1, 4, 2, 3])
overall, goal = walk_maze(code, [1, 3, 2, 4])
for vec in first.keys():
    if first[vec] == "#":
        overall[vec] = "#"

print("Part One: {}".format(part_one(overall, goal)))
print("Part Two: {}".format(part_two(overall, goal)))
