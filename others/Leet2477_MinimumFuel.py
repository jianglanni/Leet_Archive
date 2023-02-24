class Solution:
    def minimumFuelCost(self, roads, seats):
        n = len(roads) + 1
        adj_list = [[] for _ in range(n)]
        for road in roads:
            adj_list[road[0]].append(road[1])
            adj_list[road[1]].append(road[0])
        parent = [-1] * n
        frontier = [0]
        visited = set()
        while len(frontier) > 0:
            center = frontier.pop(0)
            visited.add(center)
            for neighbor in adj_list[center]:
                if neighbor in visited:
                    continue
                parent[neighbor] = center
                frontier.append(neighbor)

        def get_all_homies_here(node):  # return (cars, persons, fuel_elapsed)
            if len(adj_list[node]) == 1 and node != 0:
                return (1, 1, 0)
            fuel = 0
            persons = 1
            for neighbor in adj_list[node]:
                if parent[node] == neighbor:
                    continue
                info = get_all_homies_here(neighbor)
                persons += info[1]
                fuel += info[2] + info[0]
            cars = persons // seats
            if persons % seats > 0:
                cars += 1
            return (cars, persons, fuel)

        capital_info = get_all_homies_here(0)
        return capital_info[2]
