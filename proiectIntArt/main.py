from exhaustive import breadth_first_search, least_cost_search
from a_star import a_star_search


def read_distances():
    # Define the cities and distances
    cities = ["A", "B", "C", "D"]
    distances = {
        "A": {
            "B": 10,
            "C": 15,
            "D": 20
        },
        "B": {
            "A": 10,
            "C": 35,
            "D": 25
        },
        "C": {
            "A": 15,
            "B": 35,
            "D": 30
        },
        "D": {
            "A": 20,
            "B": 25,
            "C": 30
        }
    }
    return cities, distances


def main():
    cities, distances = read_distances()

    print("Breadth-First Search")
    bfs_path, bfs_cost = breadth_first_search(cities, distances)
    print(f"Path: {bfs_path}, Cost: {bfs_cost}")

    print("\nLeast-Cost Search")
    lcs_path, lcs_cost = least_cost_search(cities, distances)
    print(f"Path: {lcs_path}, Cost: {lcs_cost}")

    print("\nA* Search")
    astar_path, astar_cost = a_star_search(cities, distances)
    print(f"Path: {astar_path}, Cost: {astar_cost}")


if __name__ == "__main__":
    main()
