import heapq


class my_searcher(object):
    def __init__(self, val, coord):
        self.val = val
        self.coord = coord

    def __lt__(self, comp):
        return self.val > comp.val


class Solution(object):
    def maximumMinimumPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        searchers = [my_searcher(grid[-1][-1], (len(grid) - 1, len(grid[0]) - 1))]
        while True:
            anchor = heapq.heappop(searchers)
            possible_locations = [(anchor.coord[0] - 1, anchor.coord[1]), (anchor.coord[0] + 1, anchor.coord[1]),
                                  (anchor.coord[0], anchor.coord[1] - 1), (anchor.coord[0], anchor.coord[1] + 1)]
            for new_location in possible_locations:
                if (not (0 <= new_location[0] < len(grid) and 0 <= new_location[1] < len(
                        grid[0]))) or new_location in visited:
                    continue
                if new_location == (0, 0):
                    return min(anchor.val, grid[0][0])
                visited.add(new_location)
                cur_val = grid[new_location[0]][new_location[1]]
                heapq.heappush(searchers, my_searcher(min(anchor.val, cur_val), new_location))


if __name__ == "__main__":
    s = Solution()
    print(s.maximumMinimumPath(
        [[3, 4, 6, 3, 4], [0, 2, 1, 1, 7], [8, 8, 3, 2, 7], [3, 2, 4, 9, 8], [4, 1, 2, 0, 0], [4, 6, 5, 4, 3]]))
