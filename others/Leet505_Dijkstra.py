import heapq


class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        # [distance, [row, col]]
        start = tuple(start)
        destination = tuple(destination)
        locked = set()
        frontier = [[0, tuple(start)]]
        while len(frontier) > 0:
            pos = frontier[0][1]
            locked.add(tuple(pos))
            # left
            if pos[1] > 0:
                i = pos[1]
                while True:
                    if i == 0 or maze[pos[0]][i-1] == 1:
                        new_pos = (pos[0], i)
                        if new_pos == destination:
                            return frontier[0][0]+(pos[1]-i)
                        elif not new_pos in locked:
                            heapq.heappush(frontier, [frontier[0][0]+(pos[1]-i), new_pos])
                        break
                    else:
                        i -= 1
            # right
            if pos[1] < len(maze[0])-1:
                i = pos[1]
                while True:
                    if i == len(maze[0])-1 or maze[pos[0]][i+1] == 1:
                        new_pos = (pos[0], i)
                        if new_pos == destination:
                            return frontier[0][0]+(i-pos[1])
                        elif not new_pos in locked:
                            heapq.heappush(frontier, [frontier[0][0]+(i-pos[1]), new_pos])
                        break
                    else:
                        i += 1
            # up
            if pos[0] > 0:
                i = pos[0]
                while True:
                    if i == 0 or maze[i-1][pos[1]] == 1:
                        new_pos = (i, pos[1])
                        if new_pos == destination:
                            return frontier[0][0]+(pos[0]-i)
                        elif not new_pos in locked:
                            heapq.heappush(frontier, [frontier[0][0]+(pos[0]-i), new_pos])
                        break
                    else:
                        i -= 1
            # down
            if pos[0] < len(maze)-1:
                i = pos[0]
                while True:
                    if i == len(maze)-1 or maze[i+1][pos[1]] == 1:
                        new_pos = (i, pos[1])
                        if new_pos == destination:
                            return frontier[0][0]+(i-pos[0])
                        elif not new_pos in locked:
                            heapq.heappush(frontier, [frontier[0][0]+(i-pos[0]), new_pos])
                        break
                    else:
                        i += 1
            heapq.heappop(frontier)
        return -1


def main():
    s = Solution()
    # Test case
    maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
    start = [0, 4]
    destination = [4, 4]
    print(s.shortestDistance(maze, start, destination))


if __name__ == "__main__":
    main()
