class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                ret.append(i)
        return ret


def main():
    s = Solution()
    print(s.targetIndices([1, 2, 5, 2, 3], 2))  # Test Case


if __name__ == "__main__":
    main()
