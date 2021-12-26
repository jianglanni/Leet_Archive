class Solution(object):
    def executeInstructions(self, n, startPos, s):
        """
        :type n: int
        :type startPos: List[int]
        :type s: str
        :rtype: List[int]
        """
        ret = [0] * len(s)
        if n == 1:
            return ret
        row = startPos[0]
        col = startPos[1]
        for i in range(len(s)):
            ret[i] = self.emulate(n, row, col, s[i:])
        return ret

    def emulate(self, n, row, col, s):
        for i in range(len(s)):
            if s[i] == 'L':
                col -= 1
            elif s[i] == "R":
                col += 1
            elif s[i] == "U":
                row -= 1
            else:
                row += 1
            if not self.tester(n, row, col):
                return i
        return len(s)

    def tester(self, n, row, col):
        return not (row < 0 or row >= n or col < 0 or col >= n)


def main():
    s = Solution()
    print(s.executeInstructions(2, [1, 1], "LURD"))  # Test case 0
    print(s.executeInstructions(3, [0, 1], "RRDDLU"))  # Test case 1


if __name__ == "__main__":
    main()
