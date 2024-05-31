from collections import deque
from itertools import permutations


def breadth_first_search(cities, distances):
    start = cities[0]
    queue = deque([(start, [start], 0)])  # (current_city, path, cost)
    min_cost = float('inf')
    best_path = []

    while queue:
        current_city, path, cost = queue.popleft()

        if len(path) == len(cities):
            cost += distances[current_city][start]  # return to start
            if cost < min_cost:
                min_cost = cost
                best_path = path + [start]
            continue

        for next_city in cities:
            if next_city not in path:
                next_cost = cost + distances[current_city][next_city]
                queue.append((next_city, path + [next_city], next_cost))

    return best_path, min_cost


def least_cost_search(cities, distances):
    start = cities[0]
    queue = [(0, start, [start])]  # (cost, current_city, path)
    min_cost = float('inf')
    best_path = []

    while queue:
        queue.sort()
        cost, current_city, path = queue.pop(0)

        if len(path) == len(cities):
            cost += distances[current_city][start]  # return to start
            if cost < min_cost:
                min_cost = cost
                best_path = path + [start]
            continue

        for next_city in cities:
            if next_city not in path:
                next_cost = cost + distances[current_city][next_city]
                queue.append((next_cost, next_city, path + [next_city]))

    return best_path, min_cost
