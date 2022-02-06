class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return num
        neg = num < 0
        num = list(str(abs(num)))
        num.sort(reverse=neg)
        for i in range(len(num)):
            if num[i] != '0':
                num[0], num[i] = num[i], num[0]
                break
        num = ''.join(num)
        if neg:
            num = '-'+num
        return int(num)


if __name__ == "__main__":
    s = Solution()
    print(s.smallestNumber(310))
    print(s.smallestNumber(-5706))
