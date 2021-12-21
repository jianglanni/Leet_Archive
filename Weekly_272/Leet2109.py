class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        ret = []
        prev = 0
        for pos in spaces:
            ret.append(s[prev:pos])
            prev = pos
        ret.append(s[prev:])
        return ' '.join(ret)


def main():
    s = Solution()
    print(s.addSpaces("LeetcodeHelpsMeLearn", [8, 13, 15]))  # Test case 0
    print(s.addSpaces("icodeinpython", [1, 5, 7]))  # Test case 1


if __name__ == "__main__":
    main()
