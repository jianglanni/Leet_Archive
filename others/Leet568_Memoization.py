class Solution(object):
    def __init__(self):
        self.dp = []
        self.flights = []
        self.days = []
        self.n = 0
        self.k = 0

    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        self.k = len(days[0])
        self.n = len(days)
        self.dp = [[-1] * (self.k) for _ in range(self.n)]
        self.flights = flights
        self.days = days
        for i in range(self.n):
            self.dp[i][-1] = days[i][-1]
            for j in range(self.n):
                if self.flights[i][j] == 1:
                    self.dp[i][-1] = max(self.dp[i][-1], days[j][-1])
        ret = self.plan(0, 0)
        return ret

    def plan(self, city, week):
        if self.dp[city][week] > -1:
            return self.dp[city][week]
        ret = self.plan(city, week + 1) + self.days[city][week]
        for j in range(self.n):
            if self.flights[city][j] == 1:
                ret = max(ret, self.plan(j, week + 1) + self.days[j][week])
        self.dp[city][week] = ret
        return ret


def main():
    s = Solution()
    flights = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    days = [[1, 3, 1], [6, 0, 3], [3, 3, 3]]
    print(s.maxVacationDays(flights, days))


if __name__ == "__main__":
    main()