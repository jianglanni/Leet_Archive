class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ret = 0
        i = 0
        while i < len(prices):
            cur = i+1
            while True:
                if cur == len(prices) or prices[cur] != prices[cur-1]-1:
                    ret += (1+cur-i) * (cur-i) // 2
                    break
                cur += 1
            i = cur
        return ret


def main():
    s = Solution()
    print(s.getDescentPeriods([3, 2, 1, 4]))  # Test case 0
    print(s.getDescentPeriods([8, 6, 7, 7]))  # Test case 1


if __name__ == "__main__":
    main()
