class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        am = 2*k+1
        if am > len(nums):
            return [-1]*len(nums)
        l = 0
        r = l + (2*k)
        sums = sum(nums[l:r+1])
        ret = []
        while r < len(nums):
            ret.append(sums//am)
            sums -= nums[l]
            l += 1
            r += 1
            if r < len(nums):
                sums += nums[r]
        ret = ([-1]*k) + ret + ([-1]*k)
        return ret


def main():
    s = Solution()
    print(s.getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], 3))  # Test case


if __name__ == "__main__":
    main()
