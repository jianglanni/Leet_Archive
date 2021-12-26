class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return True
        num = str(num)
        return num[-1] != '0'


def main():
    s = Solution()
    print(s.isSameAfterReversals(526))  # Test case 0
    print(s.isSameAfterReversals(12300))  # Test case 1


if __name__ == "__main__":
    main()
