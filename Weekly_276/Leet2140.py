class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        dp = [-1]*len(questions)
        dp[-1] = questions[-1][0]
        pos = len(questions)-2
        while pos >= 0:
            skip = dp[pos+1]
            solve = questions[pos][0]
            if pos+questions[pos][1]+1 < len(questions):
                solve += dp[pos+questions[pos][1]+1]
            dp[pos] = max(skip, solve)
            pos -= 1
        return dp[0]


def main():
    s = Solution()
    questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
    print(s.mostPoints(questions))
    questions = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    print(s.mostPoints(questions))


if __name__ == "__main__":
    main()
