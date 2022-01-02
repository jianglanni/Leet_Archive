class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        find_b = False
        for c in s:
            if c == 'a':
                if find_b:
                    return False
            else:
                find_b = True
        return True


def main():
    s = Solution()
    print(s.checkString("aaabbb"))


if __name__ == "__main__":
    main()
