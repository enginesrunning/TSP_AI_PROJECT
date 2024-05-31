import heapq


def mst_heuristic(remaining_cities, distances):
    if not remaining_cities:
        return 0

    mst_cost = 0
    visited = set()
    edges = [(0, remaining_cities[0])]  # (cost, city)

    while edges and len(visited) < len(remaining_cities):
        cost, city = heapq.heappop(edges)
        if city not in visited:
            visited.add(city)
            mst_cost += cost
            for next_city in remaining_cities:
                if next_city != city and next_city not in visited:
                    heapq.heappush(edges,
                                   (distances[city][next_city], next_city))

    return mst_cost


def a_star_search(cities, distances):
    start = cities[0]
    queue = [(0, start, [start], 0)]  # (priority, current_city, path, cost)
    min_cost = float('inf')
    best_path = []

    while queue:
        queue.sort()
        _, current_city, path, cost = heapq.heappop(queue)

        if len(path) == len(cities):
            cost += distances[current_city][start]  # return to start
            if cost < min_cost:
                min_cost = cost
                best_path = path + [start]
            continue

        remaining_cities = [city for city in cities if city not in path]
        for next_city in remaining_cities:
            next_cost = cost + distances[current_city][next_city]
            h = mst_heuristic(remaining_cities, distances)
            heapq.heappush(
                queue,
                (next_cost + h, next_city, path + [next_city], next_cost))

    return best_path, min_cost
