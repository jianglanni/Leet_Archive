class Solution:
    def countPaths(self, grid) -> int:
        dp = [[-1] * len(grid[0]) for _ in range(len(grid))]

        def querier(row, col):
            if dp[row][col] != -1:
                return dp[row][col]
            dp[row][col] = 1
            # up
            if row > 0 and grid[row - 1][col] > grid[row][col]:
                dp[row][col] += querier(row - 1, col)
            # down
            if row < len(grid) - 1 and grid[row + 1][col] > grid[row][col]:
                dp[row][col] += querier(row + 1, col)
            # left
            if col > 0 and grid[row][col - 1] > grid[row][col]:
                dp[row][col] += querier(row, col - 1)
            if col < len(grid[0]) - 1 and grid[row][col + 1] > grid[row][col]:
                dp[row][col] += querier(row, col + 1)
            dp[row][col] %= 1000000007
            return dp[row][col]

        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ret += querier(i, j)
                ret %= 1000000007
        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.countPaths([[1], [2]]))
    print(s.countPaths([[1, 1], [3, 4]]))
