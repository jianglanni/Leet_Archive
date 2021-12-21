class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        mini = nums[0]
        maxi = nums[0]
        min_pos = 0
        max_pos = 0
        for i in range(len(nums)):
            if nums[i] < mini:
                mini = nums[i]
                min_pos = i
            if nums[i] > maxi:
                maxi = nums[i]
                max_pos = i
        critical = sorted([min_pos, max_pos])
        return min((critical[0]+1+len(nums)-critical[1]), critical[1]+1, len(nums)-critical[0])


def main():
    s = Solution()
    print(s.minimumDeletions([2, 10, 7, 5, 4, 1, 8, 6]))  # Test case 0
    print(s.minimumDeletions([0, -4, 19, 1, 8, -2, -3, 5]))  # Test case 1


if __name__ == "__main__":
    main()
