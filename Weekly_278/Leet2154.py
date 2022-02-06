class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        nums = set(nums)
        while original in nums:
            original *= 2
        return original


if __name__ == "__main__":
    s = Solution()
    print(s.findFinalValue([5, 3, 6, 1, 12], 3))