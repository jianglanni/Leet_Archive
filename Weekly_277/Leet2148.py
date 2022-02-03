class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ret = 0
        small = nums[0]
        big = nums[-1]
        for n in nums:
            if small < n < big:
                ret += 1
        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.countElements([11, 7, 2, 15]))
    print(s.countElements([-3, 3, 3, 90]))
