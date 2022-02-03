class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        positive = []
        negative = []
        for n in nums:
            if n > 0:
                positive.append(n)
            else:
                negative.append(n)
        ret = []
        for i in range(len(positive)):
            ret.append(positive[i])
            ret.append(negative[i])
        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.rearrangeArray([3, 1, -2, -5, 2, -4]))
