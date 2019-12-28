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


def path_find(start, goal, maze, heuristic, neighbours):
    priority = PriorityQueue((0, start))
    came_from = {start: None}
    costs = {start: 0}
    while not priority.empty():
        current = priority.pop()
        if current == goal:
            break
        for next in neighbours(maze, current):
            new_cost = costs[current] + 1
            if next not in costs.keys() or new_cost < costs[next]:
                costs[next] = new_cost
                priority.add(next, new_cost + heuristic(next, goal))
                came_from[next] = current
    return costs[goal]
