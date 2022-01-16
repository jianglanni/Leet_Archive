class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        step = 0
        while target > 1 and maxDoubles > 0:
            if target % 2 == 0:
                maxDoubles -= 1
                target = target // 2
            else:
                target -= 1
            step += 1
        step += target-1
        return step


def main():
    s = Solution()
    print(s.minMoves(19, 2))


if __name__ == "__main__":
    main()