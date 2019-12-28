from collections import deque
import heapq


class PriorityQueue:
    def __init__(self, *args):
        self.elements = [*args]

    def empty(self):
        return not self.elements

    def add(self, element, priority):
        heapq.heappush(self.elements, (priority, element))

    def pop(self):
        return heapq.heappop(self.elements)[1]


def reconstruct_path(came_from, current):
    path = deque([current])
    while current in came_from.keys():
        current = came_from[current]
        path.appendleft(current)
    return path


def path_find(start, goal, maze, heuristic, neighbours):
    priority = PriorityQueue((0, start))
    came_from = {start: None}
    costs = {start: 0}
    while not priority.empty():
        current = priority.pop()
        if current == goal:
            break
        for next in neighbours(maze, current):
            new_cost = costs[current]
            if next not in costs.keys() or new_cost < costs[next]:
                costs[next] = new_cost
                priority.add(next, new_cost + heuristic(next, goal))
                came_from[next] = current
    return reconstruct_path(came_from, goal)
